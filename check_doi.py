"""DOI 檢查：讀建置產物 weekNN/index.html，檢查每份講義參考文獻的 DOI。

  python3 check_doi.py            # 檢查已有的 DOI 連結：是否存在、登記的標題是否和書目相符
  python3 check_doi.py --suggest  # 另外替沒有 DOI 的書目到 Crossref 找候選 DOI（只列出，不改檔）

需要網路；只用 Python 標準函式庫。有 DOI 不存在或標題不符時結束代碼為 1。
沒有 DOI 的書目不算錯（老師規定：沒有沒關係），候選 DOI 要人工或 doi-checker agent 確認後才能加。
"""
import re,json,html,sys,time,difflib,subprocess,urllib.parse
from pathlib import Path

ROOT=Path(__file__).resolve().parent
UA='2026-QDS-doi-check/1.0 (mailto:drhhtang@mail.ntust.edu.tw)'   # Crossref 建議附聯絡信箱
# 講義裡刻意保留、不檢查的 DOI（與 build.py 的 APA_OK 對應）
SKIP={'10.1037/edu0000456'}   # APA 講義的虛構範例書目

def get(url):
    """用系統 curl 取 JSON（python.org 版 Python 在 macOS 預設沒有 SSL 憑證）；404 回傳 None。"""
    for i in range(3):
        r=subprocess.run(['curl','-sS','-L','--max-time','20','-A',UA,'-w','\n%{http_code}',url],capture_output=True,text=True)
        body,_,code=r.stdout.rpartition('\n')
        if code=='404': return None
        if r.returncode==0 and code=='200':
            try: return json.loads(body)
            except ValueError: pass
        time.sleep(1+i)
    raise SystemExit('連不上 '+url+'，請確認網路後再試')

def norm(s):
    s=html.unescape(re.sub(r'<[^>]+>','',s)).lower()
    return re.sub(r'[^a-z0-9à-ÿ]+',' ',s).strip()

def title_match(title,ref):
    """登記的標題（去掉副標也可）是否出現在書目文字裡；回傳 0–1 的相似度。"""
    t,r=norm(title),norm(ref)
    if not t: return 0
    if t in r or t.split(' ')[:6]==[w for w in t.split(' ')[:6] if w in r.split(' ')]: return 1.0
    return difflib.SequenceMatcher(None,t,r[:len(t)*2]).find_longest_match(0,len(t),0,min(len(r),len(t)*2)).size/len(t)

REF=re.compile(r'<(p|li)\b[^>]*>((?:(?!</\1>).)*?\((?:19|20)\d\d[a-z]?(?:, [^)]{1,20})?\)\.(?:(?!</\1>).)*)</\1>',re.S)
DOI=re.compile(r'https?://(?:dx\.)?doi\.org/([^\s"<>]+?)(?=[\s"<>]|\.?$|\.<)')

def refs():
    """(堂次, 分頁, 分頁名稱, 書目 HTML)"""
    for f in sorted(ROOT.glob('week[0-9][0-9]/index.html')):
        n=int(f.parent.name[4:])
        s=f.read_text(encoding='utf-8')
        d=json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>',s,re.S).group(1).replace('<\\/','</'))
        for i,doc in enumerate(d['docs'],1):
            h=re.sub(r'<(script|style)\b[\s\S]*?</\1>','',doc['h'])
            seen=set()
            for m in REF.finditer(h):
                body=m.group(2)
                txt=norm(body)
                if txt in seen or not re.match(r'^\s*(?:<[^>]+>\s*)*[A-ZÀ-Þ]',body): continue
                seen.add(txt); yield n,i,doc['t'],body

def main():
    suggest='--suggest' in sys.argv
    bad=[]; ok=0; unverified=[]; missing=[]; cache={}
    for n,i,t,body in refs():
        where='第%d堂分頁 %d「%s」'%(n,i,t)
        text=html.unescape(re.sub(r'<[^>]+>','',body)).strip()
        dois=sorted(set(DOI.findall(body)))
        if not dois:
            missing.append((where,text)); continue
        for doi in dois:
            if doi in cache or doi in SKIP: continue
            h=get('https://doi.org/api/handles/'+urllib.parse.quote(doi,safe='/()'))
            if not h or h.get('responseCode')!=1:
                bad.append('%s\n    DOI 不存在：%s\n    %s'%(where,doi,text[:160])); cache[doi]=0; continue
            cr=get('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='/()'))
            if not cr:                              # 不是 Crossref 登記的（如 DataCite），只能確認存在
                unverified.append('%s  %s'%(where,doi)); cache[doi]=1; continue
            title=(cr['message'].get('title') or [''])[0]
            if title_match(title,body)<0.8:
                bad.append('%s\n    DOI 標題和書目不符：%s\n    登記標題：%s\n    講義書目：%s'%(where,doi,title,text[:160]))
            else: ok+=1
            cache[doi]=1
    print('DOI 檢查：%d 筆相符'%ok)
    if unverified: print('\n只確認存在、無法比對標題（非 Crossref 登記）：\n  '+'\n  '.join(unverified))
    if bad: print('\n需要修正（%d）：\n'%len(bad)+'\n'.join(bad))
    print('\n沒有 DOI 的書目：%d 筆（不算錯）'%len(missing))
    if suggest:
        for where,text in missing:
            q=urllib.parse.quote(text[:300])
            r=get('https://api.crossref.org/works?rows=3&query.bibliographic='+q)
            yr=re.search(r'\((\d{4})',text); yr=yr and yr.group(1)
            cands=[]
            for it in (r or {}).get('message',{}).get('items',[]):
                title=(it.get('title') or [''])[0]
                sim=title_match(title,text)
                y=str(((it.get('issued') or {}).get('date-parts') or [[None]])[0][0])
                if sim>=0.8: cands.append('%s | %s | %s | %s | 年份%s'%(it['DOI'],title[:70],it.get('type'),y,'相同' if y==yr else '不同'))
            print('\n%s\n  %s\n  候選：%s'%(where,text[:160],('\n        '.join(cands) if cands else '（找不到標題相符的）')))
    sys.exit(1 if bad else 0)

if __name__=='__main__': main()
