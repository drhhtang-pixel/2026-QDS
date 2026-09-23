import re,json,gzip,base64,html
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'sources'
TOTAL=16          # 本學期總堂數
FAMARK='<!--FA_INLINE-->'
UUID=r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

def read(p): return open(p,encoding='utf-8').read()

def unbundle(path):
    """拆解打包格式講義，回傳 (HTML, Font Awesome CSS)。FA 字型以 woff2 data URI 內嵌。"""
    s=read(path)
    man=json.loads(re.search(r'<script type="__bundler/manifest">(.*?)</script>',s,re.S).group(1))
    tpl=json.loads(re.search(r'<script type="__bundler/template">(.*?)</script>',s,re.S).group(1))
    def raw(k):
        d=base64.b64decode(man[k]['data']); return gzip.decompress(d) if man[k].get('compressed') else d
    m=re.search(r'<style>(/\*!\s*\* Font Awesome Free.*?)</style>',tpl,re.S)
    fa=m.group(1)
    fa=re.sub(r',url\("[0-9a-f-]{36}"\) format\("truetype"\)','',fa)
    fa=re.sub(r'url\("([0-9a-f-]{36})"\)',lambda mm:'url(data:font/woff2;base64,'+base64.b64encode(raw(mm.group(1))).decode()+')',fa)
    tpl=tpl.replace(m.group(0),FAMARK)
    # tailwind: use CDN tag (allowed host) instead of inlined copy
    tpl=re.sub(r'<script src="%s"></script>'%UUID,'<script src="https://cdn.tailwindcss.com"></script>',tpl)
    assert not re.search(UUID,tpl), 'leftover uuid'
    return tpl,fa

def plain(path):
    """一般講義：把 cdnjs 的 Font Awesome <link> 換成標記，由外框頁注入共用 FA CSS。"""
    h=read(path)
    h,n=re.subn(r'<link[^>]*font-awesome[^>]*>',FAMARK,h); assert n==1,path
    return h

# 共用 Font Awesome CSS（取自第三堂 Critical Form 打包檔）
_,FA=unbundle(SRC/'week03'/'The_Secrets_of_Critical_Form_for_Reading_Papers.html')

# ─── 各堂講義 ───────────────────────────────────────────────
# 每堂回傳 [(分頁名稱, HTML, 更新紀錄)]，順序即上課講述順序。
# 更新紀錄：修改某分頁時在該分頁的清單末尾附加 ('YYYY/MM/DD','說明')。

def week03():
    U=SRC/'week03'
    tpl,_=unbundle(U/'The_Secrets_of_Critical_Form_for_Reading_Papers.html')
    BG_OLD=[('Background是指文章中值得你筆記下來的知識。','Background是指文章中奠基研究的知識。'),
     ('所搜集到的Background會是一段完整的句子。','所搜集到的Background，建議用一段完整的句子描述。'),
     ('Background通常會出現在第四章結果之前的章節，尤其是文獻探討部份。','Background通常會出現在第貳章文獻探討之前的段落，也可以包含文獻探討部份。'),
     ('通常在學者專家的人名和年份之後的那一段話，就有可能是背景。','通常有引用學者專家的人名和年份的那一段話，就有可能是背景知識。')]
    for a,b in BG_OLD:
        assert tpl.count(a)==1,a; tpl=tpl.replace(a,b)

    h=plain(U/'apa.html')
    # 懸掛縮排改套在每筆 <p> 上（原本套在外框，被 p-3 蓋掉 padding，首行跑出框外）
    a=""".citation-entry {
            text-indent: -2em;
            padding-left: 2em;
        }"""
    assert h.count(a)==1; h=h.replace(a,""".citation-entry > p {
            text-indent: -2em;
            padding-left: 2em;
        }""")
    # 「提倡包容性與多元語言」卡片加說明連結，點選開啟無偏見語言面板（apa_bias_free.html）
    a='規範性別、種族、身心障礙等議題的客觀用語，強調去偏見與包容性的學術溝通方式。</p>'
    assert h.count(a)==1; h=h.replace(a,a+'''
                    <button type="button" onclick="openBiasFree()" class="mt-3 inline-flex items-center text-xs font-semibold text-brand-600 hover:text-brand-700 hover:underline"><i class="fa-solid fa-circle-info mr-1.5"></i>了解更多：無偏見語言指引<i class="fa-solid fa-arrow-right ml-1.5 text-[10px]"></i></button>''')
    assert h.count('</body>')==1
    apa=h.replace('</body>',read(U/'apa_bias_free.html')+'</body>')

    h=plain(U/'Natural_Intelligence_in_Design_answer.html')
    a='Natural intelligence in design, Design Studies, 20, 25-39.'
    assert h.count(a)==2; ni1=h.replace(a,'Natural intelligence in design. <em>Design Studies, 20</em>, 25–39.')

    h=plain(U/'natural_intelligence_design_AI.html')
    a='<em>Design Studies</em>, 20(1), 25–39.'; assert h.count(a)==1
    h=h.replace(a,'<em>Design Studies, 20</em>(1), 25–39.')
    a='Natural intelligence in design. Design Studies, 20(1), 25–39.'; assert h.count(a)==1
    ni2=h.replace(a,'Natural intelligence in design. <em>Design Studies, 20</em>(1), 25–39.')

    return [
     ('Critical Form 閱讀論文的秘訣',tpl,
      [('2026/09/23','加入網站'),('2026/09/23','修正 Background 四點說明')]),
     ('APA 第七版格式指南',apa,
      [('2026/09/23','加入網站'),('2026/09/23','修正參考文獻範例首行超出外框'),('2026/09/23','「提倡包容性與多元語言」加上無偏見語言指引說明')]),
     ('學術資料庫比較',plain(U/'Google_Scholar_vs_Scopus_vs_WoS_vs_SDOL.html'),
      [('2026/09/23','加入網站')]),
     ('AI 質化研究工具',plain(U/'AI質化研究工具與平台全覽指南.html'),
      [('2026/09/23','加入網站')]),
     ('Natural Intelligence 解答 by drhhtang',ni1,
      [('2026/09/23','加入網站'),('2026/09/23','分頁名稱改為「Natural Intelligence 解答 by drhhtang」'),('2026/09/23','參考文獻期刊名與卷號改為斜體（APA）'),('2026/09/23','參考文獻標點依 APA 修正（標題後句點、頁碼 en dash）')]),
     ('Natural Intelligence 解答 by AI',ni2,
      [('2026/09/23','加入網站'),('2026/09/23','分頁名稱改為「Natural Intelligence 解答 by AI」'),('2026/09/23','參考文獻期刊名與卷號改為斜體（APA）')]),
     ('商學院學術資料庫',plain(U/'business_db.html'),
      [('2026/09/23','新增講義')]),
    ]

# 已上線的堂數 → 建置函式；新增一堂就在這裡加一行
WEEKS={3:week03}

# ─── 建置 ───────────────────────────────────────────────────
CN='零一二三四五六七八九十'
def cn(n): return CN[n] if n<=10 else '十'+(CN[n-10] if n>10 else '')

shell=read(ROOT/'shell.html')
cards=[]; built={}
for n in range(1,TOTAL+1):
    if n in WEEKS:
        docs=WEEKS[n]()
        for t,h,lg in docs: assert lg,t
        title='第%s堂課講義'%cn(n); key='week%02d'%n
        payload=json.dumps({'title':title,'key':key,'fa':FA,'mark':FAMARK,
            'docs':[{'t':t,'h':h,'log':lg} for t,h,lg in docs]},ensure_ascii=False).replace('</','<\\/')
        out=ROOT/key/'index.html'; out.parent.mkdir(exist_ok=True)
        page=shell.replace('/*TITLE*/',title).replace('/*PAYLOAD*/',payload)
        out.write_text(page,encoding='utf-8')
        upd=max(d for _,_,lg in docs for d,_ in lg)
        built[n]=(key,docs,upd)
        print('%s/index.html  %d 份講義  %.2f MB'%(key,len(docs),len(page)/1e6))
latest=max(built)
for n in range(1,TOTAL+1):
    if n in built:
        key,docs,upd=built[n]
        items=''.join('<li>%s</li>'%html.escape(t) for t,_,_ in docs)
        cards.append('''    <li><a class="card" href="%s/">
      <div class="head"><span class="no">%02d</span><div><b>第 %d 堂</b><small>%d 份講義</small></div>%s</div>
      <ol>%s</ol>
      <div class="meta"><span>最後更新 %s</span><em>進入 →</em></div>
    </a></li>'''%(key,n,n,len(docs),'<span class="new">最新</span>' if n==latest else '',items,upd))
    else:
        cards.append('''    <li><div class="card off" aria-disabled="true">
      <div class="head"><span class="no">%02d</span><div><b>第 %d 堂</b><small>尚未開放</small></div></div>
    </div></li>'''%(n,n))
home=read(ROOT/'home.html').replace('/*WEEKS*/','\n'.join(cards))
home=home.replace('/*SUMMARY*/','已開放 %d / %d 堂'%(len(built),TOTAL))
home=home.replace('/*UPDATED*/',max(u for _,_,u in built.values()))
(ROOT/'index.html').write_text(home,encoding='utf-8')
print('index.html  課程目錄')
