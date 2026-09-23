import re,json,gzip,base64
from pathlib import Path
ROOT=Path(__file__).resolve().parent
U=str(ROOT/'sources')+'/'
# 1. unbundle Critical Form
s=open(U+'The_Secrets_of_Critical_Form_for_Reading_Papers.html',encoding='utf-8').read()
man=json.loads(re.search(r'<script type="__bundler/manifest">(.*?)</script>',s,re.S).group(1))
tpl=json.loads(re.search(r'<script type="__bundler/template">(.*?)</script>',s,re.S).group(1))
def raw(k):
    d=base64.b64decode(man[k]['data']); return gzip.decompress(d) if man[k].get('compressed') else d
js='8e18a2ae-fc5e-4018-bef2-4af8e84440c9'
# FA css block -> extract, woff2 only
m=re.search(r'<style>(/\*!\s*\* Font Awesome Free.*?)</style>',tpl,re.S)
fa=m.group(1)
fa=re.sub(r',url\("[0-9a-f-]{36}"\) format\("truetype"\)','',fa)
fa=re.sub(r'url\("([0-9a-f-]{36})"\)',lambda mm:'url(data:font/woff2;base64,'+base64.b64encode(raw(mm.group(1))).decode()+')',fa)
FAMARK='<!--FA_INLINE-->'
tpl=tpl.replace(m.group(0),FAMARK)
# tailwind: use CDN tag (allowed host) instead of inlined copy
tpl=tpl.replace('<script src="%s"></script>'%js,'<script src="https://cdn.tailwindcss.com"></script>')
assert not re.search(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',tpl), 'leftover uuid'

BG_OLD=[('Background是指文章中值得你筆記下來的知識。','Background是指文章中奠基研究的知識。'),
 ('所搜集到的Background會是一段完整的句子。','所搜集到的Background，建議用一段完整的句子描述。'),
 ('Background通常會出現在第四章結果之前的章節，尤其是文獻探討部份。','Background通常會出現在第貳章文獻探討之前的段落，也可以包含文獻探討部份。'),
 ('通常在學者專家的人名和年份之後的那一段話，就有可能是背景。','通常有引用學者專家的人名和年份的那一段話，就有可能是背景知識。')]
for a,b in BG_OLD:
    assert tpl.count(a)==1,a; tpl=tpl.replace(a,b)
docs=[('Critical Form 閱讀論文的秘訣',tpl)]
files=[('APA 第七版格式指南','apa.html'),
 ('學術資料庫比較','Google_Scholar_vs_Scopus_vs_WoS_vs_SDOL.html'),
 ('AI 質化研究工具','AI質化研究工具與平台全覽指南.html'),
 ('Natural Intelligence 解答 by drhhtang','Natural_Intelligence_in_Design_answer.html'),
 ('Natural Intelligence 解答 by AI','natural_intelligence_design_AI.html'),
 ('商學院學術資料庫','business_db.html')]
for label,f in files:
    h=open(U+f,encoding='utf-8').read()
    h,n=re.subn(r'<link[^>]*font-awesome[^>]*>',FAMARK,h); assert n==1,f
    if f=='apa.html':
        # 懸掛縮排改套在每筆 <p> 上（原本套在外框，被 p-3 蓋掉 padding，首行跑出框外）
        a=""".citation-entry {
            text-indent: -2em;
            padding-left: 2em;
        }"""
        assert h.count(a)==1; h=h.replace(a,""".citation-entry > p {
            text-indent: -2em;
            padding-left: 2em;
        }""")
        # 「提倡包容性與多元語言」卡片加說明連結，點選開啟無偏見語言面板（sources/apa_bias_free.html）
        a='規範性別、種族、身心障礙等議題的客觀用語，強調去偏見與包容性的學術溝通方式。</p>'
        assert h.count(a)==1; h=h.replace(a,a+'''
                    <button type="button" onclick="openBiasFree()" class="mt-3 inline-flex items-center text-xs font-semibold text-brand-600 hover:text-brand-700 hover:underline"><i class="fa-solid fa-circle-info mr-1.5"></i>了解更多：無偏見語言指引<i class="fa-solid fa-arrow-right ml-1.5 text-[10px]"></i></button>''')
        assert h.count('</body>')==1
        h=h.replace('</body>',open(U+'apa_bias_free.html',encoding='utf-8').read()+'</body>')
    if f=='Natural_Intelligence_in_Design_answer.html':
        a='Natural intelligence in design, Design Studies, 20, 25-39.'
        assert h.count(a)==2; h=h.replace(a,'Natural intelligence in design. <em>Design Studies, 20</em>, 25–39.')
    if f=='natural_intelligence_design_AI.html':
        a='<em>Design Studies</em>, 20(1), 25–39.'; assert h.count(a)==1
        h=h.replace(a,'<em>Design Studies, 20</em>(1), 25–39.')
        a='Natural intelligence in design. Design Studies, 20(1), 25–39.'; assert h.count(a)==1
        h=h.replace(a,'Natural intelligence in design. <em>Design Studies, 20</em>(1), 25–39.')
    docs.append((label,h))

# 各分頁更新紀錄（新的在後面）
LOG=[
 [('2026/09/23','加入網站'),('2026/09/23','修正 Background 四點說明')],
 [('2026/09/23','加入網站'),('2026/09/23','修正參考文獻範例首行超出外框'),('2026/09/23','「提倡包容性與多元語言」加上無偏見語言指引說明')],
 [('2026/09/23','加入網站')],
 [('2026/09/23','加入網站')],
 [('2026/09/23','加入網站'),('2026/09/23','分頁名稱改為「Natural Intelligence 解答 by drhhtang」'),('2026/09/23','參考文獻期刊名與卷號改為斜體（APA）'),('2026/09/23','參考文獻標點依 APA 修正（標題後句點、頁碼 en dash）')],
 [('2026/09/23','加入網站'),('2026/09/23','分頁名稱改為「Natural Intelligence 解答 by AI」'),('2026/09/23','參考文獻期刊名與卷號改為斜體（APA）')],
 [('2026/09/23','新增講義')],
]
assert len(LOG)==len(docs)
payload=json.dumps({'fa':fa,'mark':FAMARK,'docs':[{'t':t,'h':h,'log':LOG[i]} for i,(t,h) in enumerate(docs)]},ensure_ascii=False).replace('</','<\\/')
shell=open(ROOT/'shell.html',encoding='utf-8').read().replace('/*PAYLOAD*/',payload)
open(ROOT/'index.html','w',encoding='utf-8').write(shell)
print(len(shell)/1e6,'MB')
