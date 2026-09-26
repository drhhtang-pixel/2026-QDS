# 2026 QDS 課程講義網站

## 專案概述

這是 Qualitative Design Studies（QDS 2026，授課：唐玄輝 Hsien-Hui TANG，drhhtang）的課程講義網站。
全學期共 **16 堂**，每堂一個頁面，該堂講義以分頁（tab）方式呈現，給修課學生瀏覽。
目前已上線：**第 3 堂**（8 份講義）、**第 4 堂**（2 份講義）。

- 使用者：授課老師本人（olddrhhtang）。溝通語言：**繁體中文**（偶爾用英文下指令）。
- **老師要求（2026/09/26）：每次修改完，一定要先把改好的頁面給老師看，等老師確認後才繼續下一步**
  （例如合併到 main、上線、再做其他修改）。老師偏好 **Artifact 卡片**（按 Open 就能看）：
  把 `weekNN/index.html` 去掉 `<!DOCTYPE>`/`<html>`/`<head>` 外殼後用 Artifact 工具發布。
  第四堂預覽 artifact：https://claude.ai/artifact/G2AEarTPktir4aeMDPED5D （之後更新請傳 `url` 發布到同一個網址）。
  Artifact 版的「課程目錄」連結與 SKILL 下載無作用，只供預覽；正式網站仍是 GitHub Pages。
- 讀者：研究所學生，會用電腦與手機瀏覽。
- 發布方式：GitHub Pages（此資料夾即 repository 根目錄）。
- 網址結構（老師選定 `/weekNN/`）：
  - `/2026-QDS/` → 課程目錄＝**課程進度表**（依研究方法分 4 單元，每堂卡片顯示日期、主題、Type、教師；
    已開放講義的堂次可點，JS 依今天日期標「本週」）
  - `/2026-QDS/week03/` → 第三堂；`/2026-QDS/week03/#2` → 第三堂第 2 份講義
  - 舊網址 `/2026-QDS/#2` 會自動轉到 `/2026-QDS/week03/#2`（home.html 開頭的腳本）
  另有一份 claude.ai 上的 artifact 版本：https://claude.ai/artifact/ENDbtkShVQv5TY8SW2iusV
  （Claude Code 無法更新該 artifact，以 GitHub Pages 為主要發布管道。）

## 檔案結構

```
2026 QDS/
├── CLAUDE.md        ← 本文件
├── build.py         ← 建置腳本：讀 sources/weekNN/ + shell.html + home.html，產生下列建置產物
├── package.json     ← 只用來安裝 Tailwind CLI（tailwindcss 3.4.17，與原 CDN 同版）；node_modules/ 不 commit
├── tw_cache/        ← 各講義預先編譯好的 Tailwind CSS 快取（要 commit；build.py 會自動清掉不再使用的）
├── shell.html       ← 單堂外框頁（課程目錄連結、分頁列、上一份/下一份、頁尾更新日期與更新紀錄）
├── home.html        ← 課程目錄頁範本
├── paper-reading-notes.skill ← 老師的讀論文技能包（zip：SKILL.md + assets/template.html），分頁 8 提供下載，老師同意公開
├── index.html       ← 建置產物：課程目錄，不要手動編輯
├── week03/index.html ← 建置產物：第三堂，單一自足檔案（約 2.4 MB），不要手動編輯
├── week04/index.html ← 建置產物：第四堂
├── private/         ← 不公開備份（.gitignore 排除，不會推上 GitHub），見下方「不公開備份」
└── sources/
    ├── week04/      ← 第四堂講義原始檔
    │   ├── Doing_Design_Thinking_critical_form.html  (分頁 1，由 Claude 依 paper-reading-notes 技能製作，可直接編輯)
    │   └── slr_cardsort_cluster.html  (分頁 2 SLR 系統文獻回顧，由 Claude 撰寫，可直接編輯)
    └── week03/      ← 第三堂各份講義原始檔
        ├── The_Secrets_of_Critical_Form_for_Reading_Papers.html   (打包格式，見下方；共用 FA CSS 也取自此檔)
        ├── apa.html
        ├── apa_bias_free.html   (APA「無偏見語言指引」說明面板，build.py 插入 apa.html；可直接編輯)
        ├── apa_quiz.html        (APA 課後小測驗面板 2 題，build.py 插入 apa.html；可直接編輯)
        ├── Google_Scholar_vs_Scopus_vs_WoS_vs_SDOL.html
        ├── AI質化研究工具與平台全覽指南.html
        ├── Natural_Intelligence_in_Design_answer.html
        ├── natural_intelligence_design_AI.html
        ├── business_db.html   (由 Claude 撰寫的新講義，可直接編輯)
        ├── paper_skill_process.html   (分頁 8，由 Claude 依下方 .md 製作，可直接編輯)
        └── 建立讀論文技能的過程紀錄.md  (分頁 8 的原始文字，老師提供)
```

## 建置

```bash
npm install           # 第一次（或換電腦）要裝一次 Tailwind CLI，需要 Node.js
python3 build.py      # 產生 index.html 與各 weekNN/index.html（Python 只用標準函式庫）
```

**每次修改後都要重新執行 build.py**，再檢查產物。

- **Tailwind 預先編譯**（2026/09/26 起）：講義原始檔照舊寫 `<script src="https://cdn.tailwindcss.com">` 和
  `tailwind.config = {...}`，build.py 的 `tailwind()` 會用 Tailwind CLI 依該份講義的內容與設定編譯 CSS，
  把兩段腳本換成 `<style>`（放在 `</head>` 前，與 CDN 注入位置相同，樣式順序不變）。建置產物不再載入 Tailwind CDN，
  瀏覽器也不會再出現「cdn.tailwindcss.com should not be used in production」警告。
- 快取鍵＝Tailwind 版本＋設定＋講義 HTML 的雜湊：講義沒改就直接用 `tw_cache/`，不需要 Node.js；
  改了講義但沒裝 CLI，build.py 會停下來提示先 `npm install`。
- 限制：CLI 只看得到檔案裡寫出來的 class 名稱。講義 JS 不要用字串拼接產生 class（如 `'bg-'+color+'-100'`），
  要寫完整名稱（目前所有講義都符合）。
- 2026/09/26 驗證：9 個分頁改用編譯版後，與 CDN 版整頁截圖逐像素相同；高亮開關、APA 小測驗／無偏見語言面板也相同。

## 課程進度表（SCHEDULE）

- 定義在 `build.py` 的 `SCHEDULE`（16 筆，順序＝堂次）：`(日期, 主題, 研究方法, 教師, Type)`。
- 來源：Notion「2026 Course Schedule Master」（公開頁 https://candy-napkin-731.notion.site/bb64ee39878941a3aa19d20cc294cb7d ，
  2026/09/23 老師提供整理後截圖）。**Notion 改了就同步改 SCHEDULE**。
- 研究方法 → 單元與色標由 `UNITS` 決定（文獻理論探討=綠、訪談=棕、個案研究=灰、口語分析=藍）；
  同一研究方法的堂次必須連續（有 assert）。教師不是 `HOST`（台科大唐玄輝教授）者自動標「業師」。
- 單堂頁標題也取自 SCHEDULE：「第三堂｜文獻與理論推導 I」。

## Notion 資料搬遷（已決事項，尚未執行）

- 範圍：只搬 2026 Course Schedule Master（17 列筆記頁、約 119 張圖、12 個 PDF），不搬 2022–2024 舊課。
- 取得方式：老師從 Notion 匯出 zip（HTML、含子頁面與檔案）放進專案資料夾，再轉成各堂「課堂筆記」分頁。
  （Notion MCP 無法存取該工作區；公開頁的非官方 API 可讀但不穩定，附件連結有時效。）
- 版權：期刊論文全文 PDF 不上網，只放 APA 書目＋DOI；業師演講截圖（如商業研究方法 68 張）與上課錄音 m4a
  不上網（講者同意後再議）；老師自己的講義、APA 指引可上網。
- 圖片需壓縮（macOS 內建 `sips` 縮到長邊 1600px），估計總量約 20–30 MB，GitHub Pages 容量足夠。

## 新增一堂課

1. 講義放到 `sources/weekNN/`（NN 為兩位數）。
2. 在 build.py 仿照 `week03()` 寫 `weekNN()`，回傳 `[(分頁名稱, HTML, 更新紀錄), ...]`，
   一般講義用 `plain(路徑)` 讀入（會自動處理 Font Awesome）；打包格式用 `unbundle(路徑)[0]`。
3. 在 `WEEKS` 加上 `NN: weekNN`。目錄頁會自動把該堂卡片變成可點，並列出分頁名稱與最後更新日。
4. 分頁名稱與順序請向老師確認（依上課講述順序）。

## 第三堂分頁（依上課講述順序，不可任意調換）

| # | 分頁名稱 | 來源檔 |
|---|---|---|
| 1 | Critical Form 閱讀論文的秘訣 | The_Secrets_of_Critical_Form_for_Reading_Papers.html |
| 2 | APA 第七版格式指南 | apa.html |
| 3 | 學術資料庫比較 | Google_Scholar_vs_Scopus_vs_WoS_vs_SDOL.html |
| 4 | AI 質化研究工具 | AI質化研究工具與平台全覽指南.html |
| 5 | Natural Intelligence 解答 by drhhtang | Natural_Intelligence_in_Design_answer.html |
| 6 | Natural Intelligence 解答 by AI | natural_intelligence_design_AI.html |
| 7 | 商學院學術資料庫 | business_db.html |
| 8 | 建立讀論文 SKILLS 的過程 | paper_skill_process.html |

分頁名稱、順序與更新紀錄定義在 `build.py` 的 `week03()` 回傳清單中。

## 第四堂分頁

| # | 分頁名稱 | 來源檔 |
|---|---|---|
| 1 | Critical Form：Doing Design Thinking | Doing_Design_Thinking_critical_form.html |
| 2 | SLR 系統文獻回顧 | slr_cardsort_cluster.html |

- 本堂文章：Micheli, P., Wilner, S. J. S., Bhatti, S. H., Mura, M., & Beverland, M. B. (2019). Doing design thinking:
  Conceptual review, synthesis, and research agenda. *Journal of Product Innovation Management, 36*(2), 124–148.
  https://doi.org/10.1111/jpim.12466
- Critical Form 依老師的 paper-reading-notes 技能（repo 內 `paper-reading-notes.skill` 的版本：Problem／Aim／Objectives 三格）
  製作，內容英文、標籤中英並列；第 5 節 C1→C9 依論文順序，Table 1～6、Figure 1 依原文數字重建。
- 老師在 PDF 上的眉批（Problem/results/contributions/significance、definition of design thinking、
  participatory design 與 design thinking 的比較、cluster analysis 只用 six attributes）都已放進對應卡片。
- 分頁 2「SLR 系統文獻回顧」（老師指定為第 2 個分頁）：
  - 內容：Tranfield, Denyer, & Smart (2003) 三階段 Phase 0–9（已對照原文 Figure 2, p. 214）、PRISMA 全名、
    卡片分類（Tullis & Wood 2004 建議 20–30 人；Nielsen 2004 認為 15 人）、集群分析、互動樹狀圖範例（示範資料）。
  - 內含跳到第三堂分頁 1、3 的連結（`../week03/#N`，`target="_top"`）。

## 不公開備份（private/）

- repository 是 public，任何推上 GitHub 的檔案學生都能下載，所以**期刊全文 PDF 一律不 commit**。
- `private/` 已列入 `.gitignore`：放在這裡的檔案只留在本機。第四堂文章 PDF 的位置：
  `private/week04/2018_Design_Thinking_Review.pdf`（老師本機需自行放入；雲端工作環境重開後不會保留）。
- 若需要雲端備份，建議另開 **private** repository 或放雲端硬碟（需老師決定）。

## 架構重點（build.py 在做什麼）

1. **第 1 份講義是「打包格式」**（`__bundler/manifest` + `__bundler/template`，資源以 gzip+base64 存放，
   執行時轉成 blob URL）。發布環境會擋 blob 腳本，所以 build.py 會把它**拆解還原**成一般 HTML：
   Tailwind 改用 `https://cdn.tailwindcss.com`，Font Awesome 的 CSS 與字型取出重用。
2. **Font Awesome 內嵌**：其他講義原本從 cdnjs 載入 FA 的 CSS，build.py 把該 `<link>` 換成標記
   `<!--FA_INLINE-->`，外框頁在執行時再注入一份共用的 FA CSS（字型以 woff2 data URI 內嵌，只存一份）。
3. **每份講義放在各自的 iframe（srcdoc）**，樣式與腳本互不干擾；iframe 在第一次點選時才建立。
4. **內容修正以「字串替換補丁」寫在 build.py 裡**，原始檔保持不動。每個補丁都有 `assert` 確認
   目標字串恰好出現預期次數，原始檔若被換掉會立刻報錯，不會默默失效。
   - 對原始上傳檔（第三堂第 1～6 份）：沿用補丁方式，或在老師同意後直接改 sources/ 檔案，二選一並保持一致。
   - business_db.html：可直接編輯。
5. 所有講義資料以 JSON 放在 `<script id="data" type="application/json">`，`</` 會被跳脫成 `<\/`
   （所以在 weekNN/index.html 裡用 grep 搜尋 `</em>` 會找不到，要搜 `<\/em>`）。
6. **講義內的 `href="#id"` 錨點連結**：srcdoc iframe 會用外框網址解析，點了會把整個外框載入 iframe。
   shell.html 在每個 iframe 載入後攔截這類點擊，改成在講義內 `scrollIntoView`（講義自己已處理的點擊不受影響）。
   講義要跳到同一堂其他分頁，用 `window.top.location.hash='N'`（分頁 8 的 `goTab(N)`）。
7. 外框頁的標題（第X堂課講義）與「記住上次分頁」的 localStorage key（`weekNN-tab`）由 build.py 依堂數帶入。

## 已完成的修改（2026/09/23）

- 建立 6 個分頁網站（上方編號分頁、上一份/下一份、方向鍵切換、網址 `#1`～`#7` 可直接指向分頁、
  記住上次看的分頁、淺色/深色模式、手機版分頁列可橫向捲動）。
- 分頁 5、6 改名為「…解答 by drhhtang」「…解答 by AI」。
- 分頁 1：Background 四點說明改為老師提供的新文字（補丁 `BG_OLD`）。
- 分頁 5、6：參考文獻 `Design Studies, 20` 改為斜體（APA）；分頁 6 期號 (1) 維持正體。
- 新增分頁 7「商學院學術資料庫」（BSP 四等級表、ABI/INFORM、WRDS、TEJ、Orbis 等，附參考資料連結）。
- 頁尾顯示「本頁最後更新」日期與「更新紀錄」面板，**各分頁日期各自獨立**。
- 分頁 5 參考文獻標點依 APA 修正：`Natural intelligence in design. *Design Studies, 20*, 25–39.`（老師同意）。
- 建立 GitHub repository 並啟用 Pages（見下方）。
- 分頁 2：參考文獻範例首行超出外框 → 懸掛縮排改套在每筆 `<p>`（補丁）。
- 分頁 2：「提倡包容性與多元語言」卡片加「了解更多：無偏見語言指引」按鈕，開啟頁內說明面板（內容在 `sources/week03/apa_bias_free.html`）。
- 改為 16 堂架構：首頁為課程目錄，第三堂移到 `/week03/`，舊網址自動轉址（老師選定 `/weekNN/` 格式）。
- 分頁 8「建立讀論文 SKILLS 的過程」：依老師提供的 .md 製作（四階段、秘笈欄位、Problem/Aim/Objectives
  前後對照、回饋表、經驗三點；「你」改為「老師」、經驗 1 的簡體字改正體；內附跳到分頁 1／5／6 的連結）。
- 分頁 8 加上下載卡片「如果你真的做不出來，可以下載這個 SKILL」（連結 `../paper-reading-notes.skill`，srcdoc 以外框網址解析）。
- 修正所有講義內 `#錨點` 連結會把外框載入 iframe 的問題（例如 APA 上方選單）。
- 首頁放上 2026 課程進度表（SCHEDULE），依研究方法分 4 單元，標示業師與本週。
- 分頁 2：最下方加「課後小測驗」卡片 → 開啟小測驗面板（Q1 Takishita 1997 出版年，單選；
  Q2 哪些部分首字大寫，複選；按「對答案」顯示對錯與解說）。
- 小測驗 Q1 依老師要求：「如果一年出一卷，《The Indexer》是哪一年創刊？」答案 **1978**（1997−20+1；
  陷阱 1977 忘了 +1）。解說附延伸：實際 1958 年創刊（Society of Indexers 官網 History 頁），早期一卷約兩年。
  Takishita 範例頁碼改 en dash（補丁）。
- 小測驗新增 Q3（Baker & Lancaster 1991 → 圖書）、Q4（Kass 1978 → 會議），選項用講義參考書目的分類名稱，
  解說附「看講義範例」按鈕（關閉面板、切到該分類 tab、捲到 #reference-list）。
- Git tag `2026.09.23` 標記改版前（單堂版）的網站。
- 2026/09/26：新增第四堂，分頁 1「Critical Form：Doing Design Thinking」；文章 PDF 不上網（`private/`）。
- 2026/09/26：Tailwind 改為建置時預先編譯（package.json + tw_cache/），全站不再載入 Tailwind CDN。
- 2026/09/26：第四堂新增分頁 2「SLR 系統文獻回顧」（Tranfield et al., 2003、PRISMA、卡片分類、集群分析）。

## 更新紀錄規則（重要）

老師要求：**網頁最下方顯示每次更新日期，各分頁依自己的更新狀況，不必一致。**

每次修改某一分頁時，在 `build.py` 該堂函式（如 `week03()`）中對應分頁的更新紀錄清單末尾**附加**一筆
`('YYYY/MM/DD', '修改說明')`，只改被修改的那一頁；新增分頁時要附上至少一筆紀錄（build.py 會檢查不可為空）。
課程目錄的「最後更新」自動取該堂所有分頁中最新的日期。
日期格式：`2026/09/23`。說明用繁體中文、簡短。

## 工作紀錄：第四堂分頁 2「SLR 系統文獻回顧」（2026/09/26，session 分支 `claude/zealous-tesla-96isa2`）

- 老師的要求：整理 systematic literature review（Tranfield, Denyer, & Smart, 2003）、card sorting、cluster analysis
  的相關訊息與做法成 HTML → 放第四堂**第 2 個分頁**，講義名稱「**SLR 系統文獻回顧**」。
- 來源檔 `sources/week04/slr_cardsort_cluster.html`（Claude 撰寫，可直接編輯）；段落：三者關係 → 方法 1 SLR →
  方法 2 卡片分類 → 方法 3 集群分析 → 互動範例 → 參考文獻（APA 7，7＋1 筆）。
- **對照原文後的更正（老師要求核對，改寫時不要改回去）**：
  - Phase 0–9 出自原文 **Figure 2**「Stages of a systematic review」（p. 214，改編自 NHS CRD 2001），不是 Figure 1
    （Figure 1 是證據等級）。各 Phase 說明已依原文改寫；原文沒有的內容（snowballing、「是否已有近期回顧」、
    protocol 列品質準則）已刪除。Phase 7 用原文的 realist synthesis／meta-synthesis（meta-ethnography 三技巧）；
    Phase 9 用原文的「evidence-informed」。
  - 三特質依原文「replicable, scientific and transparent process」（p. 209），不是 inclusive。
  - Tullis & Wood (2004) 建議 **20–30 人**（以 168 人為基準，15 人 r≈0.90、30 人 r≈0.95）；「15 人」是
    Nielsen (2004, NN/g) 的建議。Tullis & Wood 連結用 ResearchGate 頁（研討會報告，無 DOI）。
  - 原文 PDF 可在 Illinois 課程網站取得（不 commit）：
    https://josephmahoney.web.illinois.edu/BADM504_Fall%202019/6_Tranfield,%20Denyer%20and%20Smart%20(2003).pdf
- 老師後續要求：PRISMA 列出全名與各字母意義（Preferred Reporting Items for Systematic reviews and Meta-Analyses）；
  dendrogram 拼法正確，加說明連結（英文 Wikipedia＋SciPy 文件；中文維基「樹狀圖」會轉到「樹狀結構」，不適用）。
- 互動範例：8 張卡、6 位參與者的**示範資料**，JS 即時算共現矩陣＋平均連結樹狀圖；0.33–0.75 之間為 4 群。
  色票用 dataviz 參考色（#2a78d6、#eb6834、#1baf7a、#eda100），群旁有文字標籤。
- 內含 `../week03/#1`、`../week03/#3` 連結（`target="_top"`，已測可跳轉）。
- 單份講義預覽 artifact：https://claude.ai/artifact/SpuTgLTJAMs2Ug1VPZbZUC（FA 內嵌，只供檢查內容）；
  整堂預覽用上方第四堂 artifact。
- 教訓：這個 session 開始時 main 已被另一個 session 加入第四堂分頁 1，推送前要先 `git fetch` 並合併 main，
  再把自己的分頁排到正確位置。

## 待決事項 / 建議（尚未執行，需老師同意）

- （目前無）

## 發布到 GitHub Pages

- Repository：https://github.com/drhhtang-pixel/2026-QDS（public，帳號 drhhtang-pixel）
- 網址：https://drhhtang-pixel.github.io/2026-QDS/（目錄）、…/week03/（第三堂）、…/week04/（第四堂）
- 已設定 `http.postBuffer`（第一次推送 2.4 MB 時連線中斷，加大後正常）。

```bash
python3 build.py
git add -A
git commit -m "更新：<簡述>"
git push
```

Pages 設定：Settings → Pages → Deploy from a branch → `main` / `(root)`。約 1 分鐘後生效。
若 repository 尚未建立，先確認老師要用的 repository 名稱與帳號，再 `git init` / 設定 remote。
推送或建立 repository 前請先向老師確認。

## 技術限制與慣例

- 每個 weekNN/index.html 必須是**單一自足檔案**，外部資源只用：`cdnjs.cloudflare.com`（腳本）、Google Fonts
  （Tailwind 已改為建置時編譯內嵌，產物不再用 `cdn.tailwindcss.com`；講義原始檔仍可照舊寫 CDN 標籤）。不要引入其他 CDN 或遠端圖片（claude.ai artifact 版本的 CSP 會擋）。
- 新講義版型沿用既有風格：Tailwind、Noto Sans TC、slate/indigo 色系、白底卡片、深色漸層頁首。
- 內容用繁體中文；書目依 APA 第 7 版（期刊名與卷號斜體）。
- 測試：`.claude/launch.json` 有 `site` 設定（`python3 -m http.server 8765`），可用內建瀏覽器開
  `http://localhost:8765/` 檢查目錄頁與 `/week03/`，逐一點 `#tab0`～`#tab6` 確認 iframe 載入、無 JS 錯誤。
  （本機沒有安裝 Playwright；file:// 會被擋，請用本機伺服器。瀏覽器可能快取舊檔，網址加 `?v=N` 強制重新載入。）
