# 2026 QDS 課程講義網站

## 專案概述

這是 Qualitative Design Studies（QDS 2026，授課：唐玄輝 Hsien-Hui TANG，drhhtang）的課程講義網站。
全學期共 **17 堂**（2026/09/29 老師新增第 17 堂 2027/01/13 總結），每堂一個頁面，該堂講義以分頁（tab）方式呈現，給修課學生瀏覽。
目前已上線：**第 1～4 堂**（單元一文獻理論探討）。**第 5～17 堂**（單元二訪談、三個案研究、四口語分析）講義全部完成（2026/09/29），加密存放，依排程在上課當天 07:00 自動公開（見「定時公開」）。
**2026/10/01 起另有新網站（登入＋分頁權限）與本網站平行運作**，見「新網站」一節；停止本網站的時間由老師決定。

- 使用者：授課老師本人（olddrhhtang）。溝通語言：**繁體中文**（偶爾用英文下指令）。
- **老師要求（2026/09/26）：每次修改完，一定要先把改好的頁面給老師看，等老師確認後才繼續下一步**
  （例如合併到 main、上線、再做其他修改）。老師偏好 **Artifact 卡片**（按 Open 就能看）：
  把 `weekNN/index.html` 去掉 `<!DOCTYPE>`/`<html>`/`<head>` 外殼後用 Artifact 工具發布。
  第四堂預覽 artifact：https://claude.ai/artifact/G2AEarTPktir4aeMDPED5D （之後更新請傳 `url` 發布到同一個網址）。
  第三堂預覽 artifact：https://claude.ai/artifact/RGT8xyprcgDfPYmopeRYp9 （同上）。
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
├── CLAUDE.md        ← 本文件（公開 repo 可見，不寫 Drive ID、帳號等識別資訊）
├── CLAUDE.local.md  ← 不公開（.gitignore），Drive 資料夾 ID、帳號；Claude Code 自動讀取；換電腦要自己複製
├── _config.yml      ← GitHub Pages（Jekyll）設定：exclude CLAUDE.md、build.py、check_doi.py、seal.py、sealed，不發布成網頁
├── seal.py          ← 把未公開講義（.gitignore 排除的 sources/weekNN/）加密成 sealed/sources.tar.gz.enc
├── sealed/          ← 加密的未公開講義（要 commit；GitHub Actions 解密後依時間建置）
├── .github/workflows/release.yml ← 每週三 07:05／07:25／07:50 自動建置、公開、開 issue 通知老師
├── build.py         ← 建置腳本：讀 sources/weekNN/ + shell.html + home.html，產生下列建置產物
├── package.json     ← 只用來安裝 Tailwind CLI（tailwindcss 3.4.17，與原 CDN 同版）；node_modules/ 不 commit
├── tw_cache/        ← 各講義預先編譯好的 Tailwind CSS 快取（要 commit；build.py 會自動清掉不再使用的）
├── shell.html       ← 單堂外框頁（課程目錄連結、分頁列、上一份/下一份、頁尾更新日期與更新紀錄）
├── home.html        ← 課程目錄頁範本
├── paper-reading-notes.skill ← 老師的讀論文技能包（zip：SKILL.md + assets/template.html），分頁 8 提供下載，老師同意公開
├── index.html       ← 建置產物：課程目錄，不要手動編輯
├── week03/index.html ← 建置產物：第三堂，單一自足檔案（約 2.4 MB），不要手動編輯
├── week04/index.html ← 建置產物：第四堂
├── private/         ← （.gitignore 排除，只在老師 Mac；2026/10/05 起備份到 Drive 存檔區 private-backup/）seal.key（加密密鑰）、preview/（老師模式建置）、
│                       teacher/unit1/（從 Notion 下載的照片、PDF、錄影連結 manifest.json，只給老師模式用）、removed/（移除的舊分頁）
│                       正式存檔區在 Google Drive，見下方「存檔區」；private/ 已備份到存檔區 private-backup/（2026/10/05，改了要再 rsync，指令在 CLAUDE.local.md）
└── sources/
    ├── week01/      ← 第一堂：intro.html（課程介紹）、homework.html（課後作業）；Claude 撰寫，可直接編輯
    ├── week02/      ← 第二堂：research_structure.html、memo.html、homework.html、img/；Claude 撰寫
    ├── week05～17/  ← 未公開（.gitignore）：各堂講義＋tabs.json（分頁名稱、檔案、更新紀錄）＋img/；改完要跑 seal.py
    ├── week04/      ← 第四堂講義原始檔（另有 home_reading.html＝分頁 4「課後作業」、img/）
    │   ├── design_thinking_history.html  (分頁 1「設計思考的歷史與重點」，由 Claude 撰寫，可直接編輯)
    │   ├── Doing_Design_Thinking_critical_form.html  (分頁 2，由 Claude 依 paper-reading-notes 技能製作，可直接編輯)
    │   └── slr_cardsort_cluster.html  (分頁 3 SLR 系統文獻回顧，由 Claude 撰寫，可直接編輯)
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
        ├── supplement_ni.html／supplement_search.html／supplement_apa.html  (2026/09/28「上課補充」片段，build.py 插入分頁 2、4、6)
        ├── homework.html   (分頁 9「課後作業」)
        ├── img/            (上課補充用的照片)
        └── 建立讀論文技能的過程紀錄.md  (分頁 8 的原始文字，老師提供)
```

## 建置

```bash
npm install           # 第一次（或換電腦）要裝一次 Tailwind CLI，需要 Node.js
python3 build.py      # 產生 index.html 與各 weekNN/index.html（Python 只用標準函式庫）
```

**每次修改後都要重新執行 build.py**，再檢查產物。

- **APA 引用格式檢查（lint，2026/09/26 起）**：build.py 建置前會掃描每一份講義（補丁後的內容，略過 script/style），
  發現以下問題就**停止建置**並列出堂次、分頁與原文，不產生任何檔案：
  英文作者後用全形括號 `Simon（1981）`、「等人」、作者間用「與／、／和」、三位以上作者沒用 et al.、
  書目頁碼用連字號 `25-39`、DOI 沒有做成連結。
  - 規則在 `APA_RULES`；確認不是錯誤的例外寫在 `APA_OK`（堂次, 分頁, 字串），目前只有 APA 講義的 DOI 格式示意與虛構範例。
  - 只檢查固定格式，不判斷書目內容對錯、不查 DOI 是否存在（見下方 DOI 檢查）。
- **DOI 檢查（需要網路，推送前執行）**：`python3 check_doi.py` 讀建置產物，逐筆確認 DOI 連結存在（doi.org）且
  Crossref 登記的標題與書目相符；有錯時結束代碼 1。`--suggest` 另外替沒有 DOI 的書目列出 Crossref 候選（多半是書評、
  後來的版本等錯誤配對，**不可直接採用**）。刻意不檢查的 DOI 寫在 `SKIP`。
  - 判斷候選 DOI、替缺 DOI 的書目找正確 DOI：用 `.claude/agents/doi-checker.md`（doi-checker agent，只回報、不改檔）。
    `.claude/agents/` 有推上 GitHub（.gitignore 只排除 `.claude/` 裡的其他檔案），雲端 session 也能用。
  - 不要把老師的 email 或帳號寫進任何會 commit 的檔案，也不要放進送給外部服務的請求（如 Crossref 的 User-Agent）。
  - 本機的 python.org 版 Python 沒有 SSL 憑證，所以腳本用系統 `curl` 連網（不要改用 urllib）。

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

- 定義在 `build.py` 的 `SCHEDULE`（17 筆，順序＝堂次）：`(日期, 主題, 研究方法, 教師, Type)`。
- 來源：Notion「2026 Course Schedule Master」（公開頁 https://candy-napkin-731.notion.site/bb64ee39878941a3aa19d20cc294cb7d ，
  2026/09/23 老師提供整理後截圖）。**Notion 改了就同步改 SCHEDULE**。
- 研究方法 → 單元與色標由 `UNITS` 決定（文獻理論探討=綠、訪談=棕、個案研究=灰、口語分析=藍）；
  同一研究方法的堂次必須連續（有 assert）。教師不是 `HOST`（台科大唐玄輝教授）者自動標「業師」。
- 單堂頁標題也取自 SCHEDULE：「第三堂｜文獻與理論推導 I」。

## Notion 資料搬遷（已被取代：2026/09/27 起 Notion 連接器可直接讀寫，不再匯出 zip；以下僅供參考）

- 範圍：只搬 2026 Course Schedule Master（17 列筆記頁、約 119 張圖、12 個 PDF），不搬 2022–2024 舊課。
- 取得方式：老師從 Notion 匯出 zip（HTML、含子頁面與檔案）放進 Google Drive「2026 QDS 存檔區/notion-export/」，再把可公開的部分轉成各堂「課堂筆記」分頁。
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
| 2 | Natural Intelligence 解答 by drhhtang | Natural_Intelligence_in_Design_answer.html |
| 3 | Natural Intelligence 解答 by AI | natural_intelligence_design_AI.html |
| 4 | 學術資料庫比較 | Google_Scholar_vs_Scopus_vs_WoS_vs_SDOL.html |
| 5 | 商學院學術資料庫 | business_db.html |
| 6 | APA 第七版格式指南 | apa.html |
| 7 | AI 質化研究工具 | AI質化研究工具與平台全覽指南.html |
| 8 | 建立讀論文 SKILLS 的過程 | paper_skill_process.html |

分頁名稱、順序與更新紀錄定義在 `build.py` 的 `week03()` 回傳清單中。
- 2026/09/26 老師調整順序（原順序 1 Critical Form、2 APA、3 資料庫比較、4 AI 工具、5 NI drhhtang、6 NI AI、7 商學院、8 SKILLS）。
  連帶修改：分頁 8 的 `goTab()` 按鈕、第四堂 SLR 的 `../week03/#4` 連結、`APA_OK` 的分頁編號（APA 講義現為 6）、
  home.html 舊網址 `/2026-QDS/#N` 依舊編號轉到新編號。**再調整順序時，這幾處都要一起改。**

## 第四堂分頁

| # | 分頁名稱 | 來源檔 |
|---|---|---|
| 1 | 設計思考的歷史與重點 | design_thinking_history.html |
| 2 | Critical Form：Doing Design Thinking | Doing_Design_Thinking_critical_form.html |
| 3 | SLR 系統文獻回顧 | slr_cardsort_cluster.html |
| 4 | 課後作業 | home_reading.html（含《創造力》分組章節報告說明） |
| 5 | 課堂抽籤 | gacha.html（iframe 嵌入 https://simple-gacha.vercel.app/ ，2026/09/30 老師指定放第 5 個） |

- 分頁 1「設計思考的歷史與重點」（2026/09/26 老師指定放第四堂第 1 個分頁，原分頁 1、2 順移為 2、3）：
  designerly thinking vs. design thinking、時間軸 1962–2013、八種論述（Johansson-Sköldberg et al., 2013，表下附完整書目）、
  六個核心概念、棘手問題詳解（wicked problems 譯為「棘手問題」，附十特徵與「結構不良問題」Simon, 1973 對照）、
  流程模型（Double Diamond、d.school、IDEO、**DITLDESIGN 三鑽**：問題梳理／設計迭代／場域驗證＋擴散，老師已確認）、
  批判與反省、課堂討論 4 題（老師改寫的版本）、參考文獻 29 筆（13 筆 DOI 已逐一驗證）。

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

## 存檔區＝老師的完整上課資料，不給學生看（2026/09/26 老師決定改用 Google Drive）

分工：
- **Google Drive「2026 QDS 存檔區」**：上課存檔（論文 PDF、錄音錄影、業師資料、筆記、Notion 匯出、學生資料）。
  老師 Mac 裝 Google Drive 桌面版即為一般資料夾、自動備份；雲端 Claude 透過 **Google Drive 連接器**讀寫
  （連接器在 https://claude.ai/customize/connectors 連接，連好後要開**新對話**才會載入）。
- **GitHub `drhhtang-pixel/2026-QDS`（public）**：只放給學生看的網站與講義，維持現狀。
- 過渡用的 GitHub 私有 repo `2026-QDS-archive` 已於 2026/09/26 由老師刪除（PDF 已移到 Google Drive）。
  **不要再建立任何存放上課資料的 GitHub repo**；存檔一律放 Google Drive。

### Google Drive 使用範圍（老師規定，2026/09/26）
- **在這個專案裡，Claude 只能讀取、寫入「2026 QDS 存檔區」及其子資料夾**
  （資料夾 ID 與所屬帳號寫在本機的 `CLAUDE.local.md`，不進公開 repo；本機沒有該檔時請向老師索取）。
- 搜尋一律加 `parentId = '<存檔區或其子資料夾 ID>'` 限定範圍；不瀏覽、不讀取、不修改存檔區以外的任何檔案或資料夾
  （包括共用雲端硬碟裡既有的「2026 QDS」資料夾）。要用存檔區外的檔案，請老師先把檔案移進存檔區，或直接上傳到對話。
- 不更改任何分享設定（不用 share_file），不刪除（不用 trash_file），除非老師明確要求。
- 注意：這是 Claude 遵守的規則；連接器本身的授權是整個 Google 帳號。要做到技術上的硬限制，
  需改用只被分享這個資料夾的專用 Google 帳號來連接（見老師決定）。

### 在 Google Drive 建立存檔區（已完成，2026/09/26）
- 位置：老師公司帳號的「我的雲端硬碟」根目錄（老師選擇另建，不放進共用雲端硬碟既有的「2026 QDS」）。
- 內容：week01～week17（week17 於 2026/10/05 補建；2026/10/05 起不再分子資料夾，檔案直接放在各週第一層；
  2026/10/08 起資料夾名稱加上課程名稱，如「week01 介紹質化設計研究 QDS」「week14 商業研究方法」，取自 build.py 的 SCHEDULE，課程調整時要一起改）、Papers、notion-export、students、private-backup、Google 文件「README｜存檔區使用說明」。
- 權限：只有老師本人（owner），未分享給任何人。
- 第四堂論文 PDF 已由老師上傳到 `week04 設計思考文獻探討 Design Thinking Literature Review/2018 Design Thinking Review.pdf`（原在 week04/papers/，2026/10/05 移到第一層）；
  同資料夾另有老師放入的 Auernhammer (2021) Stanford design thinking、2024 AI 與美妝消費兩篇 PDF。
- 大檔案（PDF 等）請老師自己上傳：連接器單次上傳容量不足以傳數百 KB 以上的檔案。
- 之後新增資料夾或檔案：先 `search_files` 確認不重複；權限保持只有老師本人。
- **Drive 資料夾 ID、網址、帳號 email 一律只寫在 `CLAUDE.local.md`（已 .gitignore），不要寫進 CLAUDE.md 或任何會 commit 的檔案。**

### 規則（不論存檔放哪裡都適用）
- **資料流向只往更公開的方向**：存檔區 → 老師同意後挑選／改寫進 `sources/weekNN/` → `build.py` → 網站。
  期刊全文不上網（只放 APA 書目＋DOI），業師資料與錄音需講者同意，學生資料永不上網。
- **防呆**：公開 repo 的 `.gitignore` 全域排除 `*.pdf`、音影檔、`*.pptx`/`*.key`、`*.docx`、`*.xlsx`/`*.csv`，並排除 `private/`；
  `build.py` 最後檢查 `git ls-files`，若公開 repo 追蹤了這些副檔名或 `private/` 路徑就停下並列出檔名。
  （公開 repo 需要放 PDF 等檔案時，要先改這兩處並經老師同意。）
- 老師把存檔資料給 Claude 處理（例如 Notion 匯出轉講義）：從 Google Drive 讀取，或由老師直接上傳到對話。

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
- 2026/09/26：第四堂新增分頁 1「設計思考的歷史與重點」，原分頁 1、2 順移為 2、3（見下方工作紀錄）。
- 2026/09/26：全站內文引用統一用 et al.＋半形括號；build.py 加 APA 引用格式檢查；新增 check_doi.py 與 doi-checker agent；
  第三堂分頁 5、6 補 Cross (1999) DOI，分頁 2 Takishita 頁碼更正為 125–126。

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

## 工作紀錄：設計思考講義、引用格式統一、DOI 檢查（2026/09/26，本機 main）

- **第四堂分頁 1「設計思考的歷史與重點」**（`sources/week04/design_thinking_history.html`，Claude 撰寫，可直接編輯）。
  老師的要求依序：研究設計思考的歷史與重點做成 HTML → wicked problem 譯為「**棘手問題**」並加詳解與「結構不良問題」
  （Simon, 1973）對照 → 加 **DITLDESIGN 三鑽**（Problem Distillation 問題梳理／Design Iteration 設計迭代／
  Field Verification 場域驗證＋Diffusion 擴散，實例 EyeBus 等；中文名與說明老師已確認正確）→
  Johansson-Sköldberg et al. (2013) 完整書目放在「八種論述」表下 → 標題改「設計思考的批判與反省」→
  「先用」改「可以用」→ 課堂討論 4 題改為老師的版本（第 3 題問五步驟與三鑽的差異）→ 放第四堂第 1 個分頁。
  - 內容依據：時間軸 1962–2013 共 25 則；Double Diamond 2004、d.school 2005、Johansson-Sköldberg et al. 八種論述
    有上網查證，其餘依一般文獻知識撰寫。參考文獻 29 筆，13 筆 DOI 逐一驗證。
- **引用格式全站統一**（老師決定）：et al.＋半形括號（取代先前另一個 session 訂的全形括號、列出全部作者的規則）。
  修改了第四堂分頁 2、3，第三堂分頁 6（補丁）；第三堂 APA 講義的中文作者範例（陳一一等（2023））是教學內容，不改。
- **APA 引用格式檢查（lint）**寫在 build.py（`APA_RULES`／`APA_OK`），第一次執行抓到第四堂分頁 2 的 DOI 未做成連結。
  上線前用 9 種錯誤寫法、11 種正確寫法測過：全部抓到、沒有誤判。
- **DOI 檢查**：`check_doi.py`（腳本）＋ `.claude/agents/doi-checker.md`（判斷候選 DOI）。實測 `--suggest` 的候選
  大多是書評或後來的版本（如 Lawson 1980 → 2006 年第 4 版、Alexander 1964 → 1968 年書評），agent 已正確排除。
  已確定沒有 DOI 的 23 筆（第四堂分頁 1 的多數老書、HBR、Core77、Fast Company 等）不必再找。
- 教訓：
  - **同一個資料夾可能同時有別的 session 在跑**（這次另一個 session 改寫了 git 歷史並強制推送）。推送前先
    `git fetch`、看 `git status -sb`；必要時用 list_sessions 查看其他 session，等它完成再推。
  - `pkill -f "python3 -"` 會連帶殺掉預覽伺服器（`python3 -m http.server`），不要用這麼寬的比對。
  - `git mv -k` 對未追蹤的檔案會靜默略過，搬新檔用一般 `mv`。
  - 內建瀏覽器有時截圖全白（面板隱藏時），改用 javascript_tool 讀 DOM 確認內容。

## 定時公開（老師規定 2026/09/27）

- **課前準備**（每堂 `sources/weekNN/prep.html`，第 N 堂上課前要完成的閱讀與作業）在上課前 7 天 07:00 公開；
  **其餘講義**在上課當天（週三）07:00（台北時間）公開。時間由 build.py 的 `opens()` 計算；`ALWAYS_OPEN` 是規則訂定前已上線的堂次。
- **公開 repo 裡只要有明文原始檔就等於公開**：未公開的 `sources/weekNN/` 列在 `.gitignore`，用 `python3 seal.py`
  加密成 `sealed/sources.tar.gz.enc` 後推送（密鑰在本機 `private/seal.key`，GitHub 上是 repository secret `QDS_SEAL_KEY`）。
  **修改任何未公開講義後都要重新執行 `seal.py` 並推送 sealed/**，否則雲端公開的是舊版。
- `.github/workflows/release.yml`：每週三 07:05／07:25／07:50 解密、建置、有新內容才推送，並開一則 issue 通知老師（GitHub email）。
  可在 Actions 頁手動執行（workflow_dispatch）。雲端建置沒有 Node.js，所以 **tw_cache/ 要包含所有講義（含未公開）的快取**，本機正常 build 一次即可。
- 老師授權：講義到時間**自動公開、不必事先同意，事後告知**。其他推送（build.py、內容修正等）照舊先給老師看。
- 預覽／**老師模式**：`python3 build.py --preview` 把全部內容建置到 `private/preview/`（不影響正式產物）：卡片連到
  `weekNN/index.html`、標出學生目前狀態與公開時間，頁首有「老師模式」提示。老師模式 artifact（只有老師看得到）：
  https://claude.ai/artifact/FJmk7vLnNMxHZq52mBnYhd —— 主頁用 `private/preview/index.html` 去掉 doctype/html/head/body 外殼，
  `files` 帶 `weekNN/index.html`。**每次修改講義後都要重新 --preview 並更新這個 artifact。**
  `QDS_NOW=2026-10-07T07:00 python3 build.py` 可模擬某個時間點（測完要再跑一次一般 build 還原）。
- **老師模式補充**（2026/10/05）：只給老師的講義放 `private/teacher/weekNN/`（`teacher.json` 指定插入既有分頁的片段、或新增分頁與位置），
  build.py 的 `teacher_extras()` 只在 `--preview` 讀入；不進公開 repo、不進 sealed、舊網站與新網站都沒有。新增分頁插在中間時，
  原分頁裡的「分頁 N」與 `location.hash` 自動順移。老師模式專用的 Tailwind 快取放 `private/tw_cache_preview/`。
- **個案客戶名稱**（2026/10/05 老師決定）：第 5 堂兩個個案一律寫 H Company、L Company（對照在 CLAUDE.local.md）；圖片與旗下品牌名暫不處理。
- 機器人會推 commit 到 main：**本機推送前一定先 `git pull --rebase`**。
- 某堂公開後：可從 `.gitignore` 移除該堂、把原始檔一般 commit；並更新 Notion 該列「網頁講義」「整理狀態＝已上線」。

## 工作紀錄：2026/09/27–28 session（Notion 整理＋單元一、二講義＋定時公開）

詳細的網址、Notion 頁面與含業師／客戶細節的決定寫在 `CLAUDE.local.md`。

### 做了什麼
1. **Notion 盤點與標示**（連接器可直接讀寫 `[課程]`）：比對 2022～2026 各年度頁面，在頁首加標示 callout：
   【母版】【重複資料】【原始頁】【內容放錯】【封存說明】【頁首】。只新增、不刪除不搬移。
   2026 資料庫改名「2026 Course Schedule Master」，新增屬性「網頁講義」（URL）、「整理狀態」（未整理／已盤點／講義完成／已上線），
   加「整理進度」看板檢視；範本「Lesson」改為四段結構（頁首 → 本年度筆記 → 講義底稿 → 相關舊資料，只放連結）；
   舊年度首頁加【封存說明】；`[課程]` 底下建立「QDS 2026 整理總覽」頁（連結、規則、講義底稿流程、標示說明、單元進度）。
2. **單元二訪談（第 5～8 堂）講義**：第 5 堂訪談方法與個案練習、第 6 堂《創造力》、第 7 堂業師課前導讀、
   第 8 堂 Eckert & Stacey (2000) Critical Form＋讀論文的提醒；各堂最後一個分頁「課後作業」。
3. **單元一文獻（第 1～4 堂）講義**：第 1 堂新增（課程介紹、課後作業）、第 2 堂新增研究架構與 MEMO、
   第 3 堂分頁 2／4／6 加「上課補充」＋分頁 9 課後作業、第 4 堂加上課補充與照片。
4. **定時公開**（見「定時公開」一節）、**老師模式**（`build.py --preview`，只有老師看得到的 artifact）、
   `check_doi.py --preview`（檢查含未公開講義的預覽建置）。
5. 盤點表、待決表、挑照片頁都用有資料庫的 artifact 讓老師勾選；勾選結果另存成靜態 HTML 放 Drive 存檔區 notion-export/。

### 老師決定的規則（之後都照做）
- **講義上課當天（週三）07:00 自動公開，不必事先同意，事後告知**；還沒公開的原始檔不可出現在公開 repo。
- **每一堂最後一個分頁是「課後作業」＝下一堂要討論的內容；論文閱讀提前兩週**（第 N 堂要討論的論文放第 N−2 堂的課後作業）。
  不再用「課前準備」分頁。自由作業要標示「自由作業」。
- **老師模式**：顯示全部內容與學生公開狀態；錄影連結、老師投影片、期刊全文 PDF 只放老師模式（來自 `private/teacher/`，不進 repo 也不進 sealed）。
  每次修改講義後都要重新 `--preview` 並更新老師模式 artifact。
- **客戶名稱**：單元一講義一律用一般化例子，不出現客戶名稱（老師：學生版匿名、老師講義用全名）。第 5 堂兩個個案 2026/10/05 起改寫 H Company、L Company（取代先前的真名）。
- **APA**：年代照原文獻著錄（民國年不改）；圖與表的編號與標題依 APA 7 都放在上方（講義已加說明）；Scopus 說法照網站（期刊、會議、叢書）。
- 講義內容以「上課補充」標籤標出由 Notion 筆記整理加入的部分；原始上傳檔（第三堂分頁 1～6）不直接改，用 build.py 插入片段。
- 資料流向維持只往更公開的方向；Notion 以外的工作區（如 DITLDESIGN 會議記錄）**先不讀**。
- **Notion「QDS 2026 整理總覽」頁是老師記進度的地方**（網址在 CLAUDE.local.md）：每次完成或新增待辦（上線、整理單元、老師要做的事），
  都要同步更新該頁的「老師的待辦／請 Claude 做的待辦／自動公開時程／單元進度／歷程」，老師靠它記得做到哪裡。

### 待辦
- ~~把 `private/` 備份到 Google Drive 存檔區~~：2026/10/05 完成（存檔區 private-backup/）。
- 老師自己刪除：2026 資料庫 4 筆「【空白列｜請老師刪除】」、「2024 Course Schedule Bachalor (1)」整個資料庫。
- 單元三個案研究（第 9～12 堂）已完成（2026/09/28）；單元四口語分析（第 13～17 堂）進行中。
- 第 7 堂上課後依今年演講更新；第 5 堂 2026/10/05 老師確認不再修改。
- 每堂自動公開後，把 Notion 該列改為「已上線」並填網頁講義網址（雲端流程不會自動更新 Notion）。

## 工作紀錄：2026/09/28–30 session（單元三個案研究、單元四口語分析、Notion 全面整理）

詳細網址、Drive 資料夾、業師與客戶的決定寫在 `CLAUDE.local.md`。

### 講義（全部已加密推送，依排程公開）
（2026/10/07 課程調整後，第 11、12、14 堂已對調，見下方「2026/10/07 課程調整」；本表保留 9/28–30 當時的堂次。）

| 堂 | 日期 | 分頁 |
|---|---|---|
| 9 | 11/04 | 個案研究：從事實推到知識（2022／2023 講課筆記）；個案練習：公共設計案與趨勢（含 5 張趨勢投影片）。無課後作業 |
| 10 | 11/11 | Critical Form：Lotus Bicycle（2026/09/30 補上，依掃描檔與老師眉批；DOI 為 10.1016/0142-694X(95)00026-N）；論文討論：蓮花腳踏車（討論導讀）；Critical Form：境隨心轉（附延伸閱讀 Cardon et al., 2011）；課後作業（Park-Lee、Steen） |
| 11 | 11/18 | 業師課前導讀：商業研究方法（只寫一般化方法、只寫講者姓名）；課後作業（自由作業：假設法） |
| 12 | 11/25 | 改名「個案研究論文討論」。Critical Form：Park-Lee (2020)、Steen et al. (2011)；課後作業（Suwa & Tversky，第 14 堂討論） |
| 13 | 12/09 | 業師課前導讀：用戶體驗研究（含 4 張講者簡報照片，附延伸閱讀 Postma et al., 2012）；課後作業 |
| 14 | 12/16 | Critical Form：Suwa & Tversky (1997)（老師 QDS 2018 筆記表＋原文＋老師眉批 25 則）；口語分析入門；課後作業（Valkenburg & Dorst） |
| 15 | 12/23 | 口語分析的做法（老師投影片：段句、編碼基模、編碼範例、新手專家比較，老師同意公開）；課堂練習：放聲思考（改寫自老師 1998 實驗指示語）；課後作業（期末預告） |
| 16 | 1/06 | Critical Form：Valkenburg & Dorst (1998)（老師 CGU 2003 筆記表＋原文）；課後作業（四單元回顧） |
| 17 | 1/13 | **新增（老師 2026/09/29 決定）**：總結（四種方法、Data→Knowledge、Simon／Schön／FBS、創造力與文化）；期末作業：設計三個實驗 |

- `build.py`：`TOTAL=17`；第 14 堂 Type＝Paper Discussion、第 15 堂＝Lecture；第 17 堂「總結」。
- 老師決定的排程（2026/10/07 調整後）：第 12 堂討論 Suwa、第 15 堂方法與練習、第 16 堂討論 Valkenburg；論文至少提前兩週指定。
- Critical Form 可交給 agent 平行寫（模型檔 `sources/week08/Eckert_Stacey_critical_form.html`），給同樣的 lint 規則；
  論文全文沒有時只用老師的筆記表，不補原文細節。掃描檔 PDF 用 pymupdf 轉頁面圖再讀（本機無 pdftoppm；scratchpad venv 裝 pypdf、pymupdf）。
- 照片流程：Notion 下載（簽名網址 5 分鐘，或用 REST API 取 1 小時連結）→ `sips` 縮 1400px → manifest.json →
  `private/logs/gen_photos_unit3.py`／`gen_photos_unit4.py` 產生挑選頁 artifact（db collection `photos`）→ 老師勾選 → 放 `sources/weekNN/img/`。

### Notion 整理（log 在 private/logs/notion_unit3_log.md、notion_unit4_log*.md、notion_cleanup_20260928_log.md）
- 17 堂都有【頁首】（第 17 堂列 2026/09/29 新建）；第 9～17 堂整理狀態＝講義完成。
- 母版／原始頁／重複資料標示補到單元三、四；2024 大學部誤標的【母版】已更正，副本改指向 2026 母版。
- 第 10、12、13 堂互放錯的筆記加【內容放錯】互連；作業欄統一為「該堂討論的論文」（舊值移到頁內「舊作業」）。
- 舊年度 2022–2024 四頁搬進「QDS 封存（2022–2024）」（老師同意搬移）；主頁索引加「現行連結」欄；舊資料庫 15 個範本加【封存範本】。
- 不可公開標示：Student list ×4、第一次作業【學生資料】、9/16 9/23 課堂逐字稿 ×4【含學生發言】（連到第 2、3 堂）、業師頁 ×3【個資】。
- 總覽頁最上方放學生網站與老師模式連結；公開時程到第 17 堂。
- API 設不了資料庫檢視篩選，已列入老師待辦（手動設定）。

### 還沒做／待老師
- 業師講座後依今年演講更新：第 7 堂（10/21）、第 14 堂（12/16，原第 11 堂）、第 13 堂（12/09，簡報照片公開前確認講者同意）。
- 每堂公開後更新 Notion「已上線」與網頁講義網址。

## 工作紀錄：2026/09/30–10/01 session（第 2、3、4、6、10 堂修改）

### 做了什麼（全部已推送上線；第 6、10 堂為加密檔，依排程公開）
- 第 3 堂分頁 9 課後作業：改為「思考如何用三個資料庫查『設計的定義』」。
- 第 4 堂分頁 1「設計思考的歷史與重點」：
  - 時間軸各則加書目（TL 陣列的 `r` 欄位，可為字串或陣列；渲染成小字＋書本圖示）：Simon、Jones、Lawson、Cross、Schön、Rowe、
    Brown 2008／2009、Martin 2009（兩本附中文版：《設計思考改造世界（十周年增訂新版）》吳莉君、陳依亭譯，聯經 2021；
    《設計思考就是這麼回事！》林麗冠、李仰淳譯，天下文化 2011）、Dorst 2011、Kimbell 2011、Johansson-Sköldberg et al. 2013、
    共同演化三篇（Maher & Poon 1996、Dorst & Cross 2001、Maher & Tang 2003；標題年份改 1996–2003）。
  - 時間軸按鈕：TL 的 `more:['openXxx','按鈕文字']` 欄位會在該則下方產生「了解更多」按鈕。
  - 跳出面板（形式同第 3 堂 APA 無偏見語言面板）：「有用的迷思」（Norman 2010＋2013 修正看法）掛在批判與反省的 details 內；
    「Bryan Lawson 做了什麼？」掛在時間軸 1980（四類研究方法、彩色積木實驗 1979 年發表、延伸影片連結）。
    老師給的 Lawson 原稿有一段「人格量表測量」與事實不符，已依老師同意改寫為「心理學觀點的整合」。影片片名照老師寫法，不改。
    時間軸 1980 說明加「配合上訪談釐清設計本質」（老師文字）。
  - 「有用的迷思」內文改為老師版本（結尾提問「你認同這樣的說法嗎？」）。
  - Double Diamond、DITLDESIGN 三鑽模型加 SVG 線稿（自繪，保留原色塊）；三鑽補 EyeBus 論文 Wang et al. (2022) IJDesign
    （DOI 10.57698/v16i1.04 非 Crossref 登記，check_doi 只能確認存在）。
- 第 4 堂分頁 4：《創造力》分組章節報告說明（全班讀第一章；第 2～7、12、13 章八組各一章；6 分鐘、6～12 頁、Critical Form）。
- 第 4 堂分頁 5：課堂抽籤（外部 iframe，是「只用 cdnjs／Google Fonts」規則的例外，老師指定；artifact 預覽會擋，正式站正常）。
- 第 6 堂（加密）：指定章節補第 7 章「早年歲月」（Claude 依一般理解撰寫，未對照原文）、章名與書一致、標出組別、分組連到第 4 堂分頁 4。
- 第 10 堂（加密）：新增分頁 1「Critical Form：Lotus Bicycle」（agent 依掃描檔 20 頁＋老師眉批撰寫；正確 DOI 為
  10.1016/0142-694X(95)00026-N）。原討論導讀改為分頁 2。p. 71 標題旁一則中文眉批看不清楚，老師說先不管。
- 第 2 堂 AIMRDR：加 A Abstract；Literature、Conclusion 改為括號內的補充項（虛線框、縮排）。
- 寫了一篇 FB 貼文（設計思考的歷史與重點）給老師自行發布，未存檔。

### 待辦
- 學生填寫分組名單：之後做。老師建 Google 表單（日期、課程、組別、組員姓名）放存檔區 students/ → 在第 4 堂分頁 5 加「填寫分組名單」按鈕；
  回覆複製姓名、組別貼進抽籤工具。學生資料不進 repo。
- ~~第 5 堂可能還要改~~（2026/10/05 確認不改）；第 7、11、13 堂業師講座後更新；第 13 堂簡報照片公開前確認講者同意。

### 教訓
- 內建瀏覽器的預覽伺服器（port 8765）隔一段時間會停，navigate 失敗時重新 `preview_start site`。
- 關閉的 `<details>` 裡元素的 innerText 是空字串，用 JS 找按鈕要用 textContent。
- 本機有 hook 會擋含刪除指令字樣的 Bash 指令；不再需要的記憶改寫成「已完成」而不是刪掉；長的 Python 先寫成檔案再執行。
- 第 7 章等未對照原文的內容要明講「依一般理解撰寫」，請老師審。

## 新網站：登入＋分頁權限（2026/10/01–03 session）

新網站 https://ditldesign-users-control.pages.dev/ 已上線，與本網站（GitHub Pages）**平行運作**。
程式、金鑰、帳號等細節**不寫在這裡**（公開 repo）：說明在私有 repo 的 `PLATFORM.md`，本機重點在 `CLAUDE.local.md`。

### 老師的需求與決定
- 五類使用者：不加入使用者（未登入）、免費使用者（註冊預設）、上課的同學、付費的同學、付費的老師；另有管理者（老師）。
  E-mail 當帳號、自設密碼；註冊填姓名、E-mail、單位、學號。
- **學號**：申請「上課的同學」必填（網頁與資料庫都檢查）；付費的同學、付費的老師可不填。
- **開課班級**（2026/10/03）：註冊時單位自由填；在「我的帳號」申請「上課的同學」時**必選班級**（今年 DT5516701、DT5516702，
  質化設計研究），單位自動變成「課號 課名」；付費身分單位自由填。後台可依班級篩選。**新增或停用班級由 Claude 加**（老師決定，不做後台介面）。
- **刪除使用者**（2026/10/03）：後台「刪除」不真的刪資料——權限等同免費使用者、排到名單最下方、可「還原」恢復原身分；管理者不能刪。
- 升級：學生在「我的帳號」申請，老師在後台核准或批次設定（貼修課名單 E-mail）；**金流之後再說**。
- 權限以分頁為單位：全開放（整門課）／單課開放（某堂）／分頁開放；**五類身分各自獨立勾選**
  （不加入使用者能看的，登入者不會自動也能看）；上層涵蓋的格子可直接取消，系統自動拆成其餘分別開放。
- 開放時間放在後台權限頁：堂＝上課日 07:00（第 1～4 堂也依上課日倒推填入），分頁可另設；時間到才開放，不必重新建置。
- 預設：第 1～4 堂五類身分都開；第 5 堂以後開給上課的同學、付費的同學、付費的老師（免費使用者看不到）。
- 後台入口：登入後右上角橘色「後台」。驗證信、重設密碼信為中文，從老師的 Gmail 寄出。
- 長遠規劃：之後可能約 8 門課，資料表一開始就分課程。
- **與舊網站平行**；第 5 堂 10/07 照常在本網站公開。本網站首頁有「新網站上線，請註冊」橫幅（build.py 的 `NEWSITE`，只放本網站）。
  新網站首頁右側「📢 註冊說明」收合面板（含 QR code），完整公告在新網站 `/register`。

### 工作方式（重要）
- 新網站的程式在**另一個資料夾**（本 repo 的 git worktree，platform 分支），只推到**私有 repo**；
  本資料夾 `.git/hooks/pre-push` 會擋下推到公開 repo 的 platform 內容。**不要把新網站程式 commit 到 main。**
- 本資料夾的 `dist/`（新網站建置產物，含講義全文）已用 `.git/info/exclude` 排除，**不可加入公開 repo**。
- 改講義照舊在本資料夾改、commit 到 main；新網站要同步時，到 worktree 執行 `./deploy.sh --content`（會先合併 main）。
- 講義內容存在 Supabase 私有存放區，網頁本身不含講義（上線前比對過 925 段講義文字，網站檔案都找不到）。
- 資料庫結構改動（supabase/migrations/）要請老師貼到 Supabase SQL Editor 執行；本機可用 pip 的 pgserver 跑權限測試。

### 交作業＋成果發表（2026/10/08 上線，只在新網站）
- 老師在後台「作業」分頁出作業（名稱、說明、班級、截止時間、公開）；學生在「交作業」選作業、寫作業內容說明、勾同班組員（姓名＋學號）、上傳單一 HTML（10 MB 內）。
- 截止後仍可交，標「遲交」；第二次起標「重交」並留每次日期。同一作業一人只能在一組。
- 「成果發表」頁所有登入者可看，點組別顯示該組 HTML（沙箱 iframe）；老師可排順序或隨機排序。學號只給同班與老師看。
- 細節（資料表、RPC、測試方式）在 PLATFORM.md；舊網站（GitHub Pages）不做。

### 切換舊網站（等老師通知，尚未執行）
停用 `.github/workflows/release.yml` → 本網站各頁改為轉址到新網站 → 確認學生已註冊並設成「上課的同學」→
未公開講義改放私有 repo，seal.py／sealed 退役。

### 教訓
- 存 `.env` 時 `=` 後面不要有空白，最後一行要換行；用 `>>` 附加前先確認檔尾有換行（這次接成同一行導致金鑰失效）。
- Gmail 應用程式密碼要去掉空白，否則 Supabase 寄信失敗（Error sending confirmation email）。
- 剪貼簿複製中文要 `LANG=en_US.UTF-8 pbcopy`，否則貼上變亂碼。
- Claude 結束回覆時 App 會關掉預覽伺服器；需要長時間給老師測試的本機伺服器改用背景執行。
- Cloudflare Pages 會把 `xxx.html` 轉成 `/xxx`（308），查詢字串保留，站內連結不受影響。
- 不能代替老師在雲端服務註冊帳號或輸入密碼；需要時請老師自己操作，登入後的畫面用本機假資料測試頁驗證。
- **不要用瀏覽器的 `confirm()`**：老師的 Chrome 曾封鎖對話方塊，confirm 直接當成「取消」，刪除按鈕看起來沒反應。
  後台一律用網頁內確認框（admin.html 的 `ask()`），並在失敗時顯示錯誤訊息。
- 資料庫改動（新增欄位、規則）一定要**先請老師執行 SQL、確認生效，再上線網頁**，否則網頁會找不到欄位而出錯。
- 學生姓名、學號、E-mail 等個資不寫進 CLAUDE.md（公開 repo）。

## 工作紀錄：2026/10/03–05 session（整理總覽、存檔區整理、第 5 堂老師模式補充、客戶匿名）

詳細網址、Drive 資料夾 ID、客戶真名對照寫在 `CLAUDE.local.md`。

### 做了什麼
- **第 5 堂**：老師看過預覽，內容不改，照排程 10/07 公開。個案客戶改寫 **H Company**（永續服務個案）、**L Company**（房屋銷售練習），
  學生版重新加密推送、新網站 `./deploy.sh --content` 同步；第 6 堂一筆舊更新紀錄一併改。投影片與照片裡的真名、旗下品牌名（Dyson、Restyle 2050、Refresh）老師說先不處理。
- **第 5 堂老師模式補充**（學生看不到）：老師提供 2023 上課簡報（Keynote，存檔區 week05/）。Keynote 用 `osascript` 輸出 PDF
  （要 `skipped slides:true` 才會含隱藏頁，頁碼才對得上 .pptx），pymupdf 轉圖。內容放 `private/teacher/week05/`：
  - 分頁 1「訪談的基礎與方法」（新增，排第一）：整理 Purdue Writing Lab 與 Valenzuela & Shrivastava (2002) 兩份英文教材，附 7 筆參考文獻（Dick、McNamara、Patton、Kvale & Brinkmann 依一般知識，未逐筆查證）。
  - 分頁 3 六階段後加「個案細看：從訪綱到三個分析框架」（訪綱四步、受訪者篩選與走查、summary 與共同／相異／特別點、體驗維度、人物誌象限、AAPR）。
  - 分頁 4 加作業範例「體驗情境板」。
  - 老師要求：**不標簡報頁數**、不用「補充」字樣與說明框。
- **build.py**：`teacher_extras()` 老師模式補充機制（見「定時公開」一節）。
- **給講者的單頁**：第 5 堂「個案與練習」轉成單一 HTML（`private/share/`，去掉跨分頁連結與本週作業），寄給照片中的專案設計師。
- **Google Drive 存檔區**：week01～16 的 guest／notes／papers／recordings 子資料夾取消（4 個檔案移到各週第一層，64 個空資料夾移除），
  補建 week17；README 由老師貼上新版說明（這個 session 沒有 Google Docs 連接器，Drive 連接器改不了文件內容）。
- **private/ 備份**到存檔區 `private-backup/`（Drive 桌面版本機路徑 rsync，只增不刪）；Notion 總覽加「資料存放地圖」圖（PNG，headless Chrome 截圖後上傳）。

### 教訓
- Notion 頁面的圖片區塊不能用 update_content 比對替換：先插入新圖，再用 REST API `delete-a-block` 刪舊圖。
- Drive 連接器只能改檔名與位置；要改 Google 文件內容需要 Google Docs 連接器（開新對話才會載入），否則寫好段落請老師貼。
- 只能在「2026 QDS 存檔區」裡操作：找本機路徑時不要列出「共用雲端硬碟」等其他資料夾。
- 老師模式的 Tailwind 快取不可寫進公開的 `tw_cache/`，preview 建置也不可清公開快取（已在 build.py 處理）。

## 2026/10/07 課程調整（業師調時間）

- 原第 12 堂（個案研究論文討論：Park-Lee、Steen）→ **第 11 堂 11/18**；原第 14 堂（口語分析：Suwa & Tversky、口語分析入門）→ **第 12 堂 11/25**；
  原第 11 堂（業師陳羿霖：商業研究方法）→ **第 14 堂 12/16**；其他不變。`sources/week11、12、14` 資料夾直接對調，`SCHEDULE` 同步。
- 單元要連續：單元三個案研究改為第 9～11 堂、單元四口語分析第 12～17 堂（第 14 堂商業研究方法歸口語分析單元，老師同意）。
- 閱讀維持至少提前兩週：第 9 堂**新增**課後作業（Park-Lee、Steen，第 11 堂討論）；第 10 堂改讀 Suwa & Tversky（第 12 堂）；
  第 11 堂＝Suwa 閱讀提醒；第 12、13 堂＝下一堂業師講座準備＋自由作業；第 14 堂＝Valkenburg & Dorst（第 16 堂）＋自由作業（假設法）。
- 講義內文的堂次與日期（Critical Form 頁首、第 7／13／15／16 堂的交叉引用）一併改；各分頁更新紀錄加「課程調整」。
- 新網站：`deploy.sh --content` 依「名稱→順序」對應分頁，第 14 堂殘留舊分頁「口語分析入門」用 service key 從 tabs 表與儲存區刪除（老師同意）。
  **教訓：堂次對調時，分頁數變少的那堂會留下舊分頁，上線後要檢查並移除。**
- Notion：資料庫三列改日期與 week 欄（商業研究方法的研究方法欄改口語分析），頁首註明調整；總覽的公開時程、單元進度、待辦已更新。

## 工作紀錄：2026/10/05–08 session（第 5 堂上課後修正、新網站重設密碼、Notion 排程）

- **第 5 堂**（10/07 已自動公開，之後的修改直接推送＋`deploy.sh --content`）：
  - 新增分頁 1「課前考試：系統文獻回顧」（`sources/week05/pre_exam.html`：SLR 步驟、設計思考與 AI 兩題；`<details>` 按了才出現的提示，連到第 4 堂分頁 3、1）。
    其餘分頁往後移，頁內「分頁 N」與 `location.hash` 一併 +1；老師模式 `teacher.json` 的 tab 編號與 pos 也跟著改（課前考試排第一、老師補充分頁排第二）。
  - 分頁 2（訪談的方法與實務）：四種出發點（桌面研究／策略／客戶內部／研究）、Personality 補「訪問者的原生個性不重要」、
    Outcome 改為「解決問題」且流程最後一格改「問題解決 Problem Solving」、「五個思考面向」、步驟說明去掉「課堂」、
    訪談人數補「專業執行…16 位選 8 位」、訪綱結構範例改為產品使用（現在→過去→未來）、「改成」範例加「您有購買這個產品嗎？」。
  - 課後作業：刪除「準備一個你想問業師的問題」與自由作業「體驗情境板」（老師模式的情境板範例保留，註明今年學生版已刪除）。
  - 老師改字時，明顯錯字（如「資收集」）照改並在回報中說明。
- **新網站重設密碼修正**（platform 分支 `platform/account.html`、`login.html`）：重設連結 `account.html#reset` 被 Supabase 接成兩個 `#`，
  supabase-js 讀不到，頁面沿用瀏覽器原本登入的帳號（老師的 gapps 帳號重設時顯示成 gmail 帳號）。改為帳號頁自行解析網址、`setSession` 切換帳號、
  顯示「正在替 E-mail 設定新密碼」；連結失效回登入頁 `?reset_error=1`。老師已用 gapps 帳號重設成功。
- **Notion 排程**：本機排程「【每週三】QDS 公開後更新 Notion 已上線」（每週三 08:30 後）。10/07 第一次執行卡在第一個指令的權限確認，
  第 5 堂改由本 session 手動標為已上線。**老師需在側邊欄 Scheduled 對該排程按一次 Run now 核准工具權限**，之後才能自動跑。
- 記憶：重要的訪談資料集合在 DITLDESIGN Confluence（網址在 CLAUDE.local.md），做訪談單元時提醒老師、讀前先問。

## 待決事項 / 建議（尚未執行，需老師同意）
- 停止舊網站並轉址到新網站（時間由老師決定，見「新網站」一節）。

- 向 GitHub Support 申請移除舊 commit 快取（見「清除 git 歷史中的 Drive ID 與帳號」）。
- 是否也把 shell.html、home.html、package*.json 加進 `_config.yml` 的 exclude（check_doi.py 已加入）。
- 若有只給修課生的內容，評估搬到 Cloudflare Pages + Access。

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

### 平台評估（2026/09/26 老師詢問後決定：繼續用 GitHub Pages）
- 適合原因：純靜態、單一自足 HTML、內容本來就公開、免費 HTTPS、push 才上線且有版本紀錄、容量足夠。
- 限制：無法設密碼／限定登入；repo 為 public（原始檔、build.py、CLAUDE.md 都看得到）；無法收學生作答資料。
- **若將來有「只給修課生看」的內容**（如講者同意後的業師簡報）→ 改用 **Cloudflare Pages + Cloudflare Access**
  （以學生 email 一次性驗證碼登入，免費 50 人內；靜態產物可直接搬）。Netlify/Vercel 密碼保護要付費，不建議；
  學校 LMS 只當入口放連結；Notion 無法放自訂 HTML/JS。

### Pages 會把 repo 裡所有檔案發布成網頁（2026/09/26 發現）
- 預設 Jekyll 會把 `CLAUDE.md` 轉成 `…/2026-QDS/CLAUDE.html`、其他檔案原樣公開。已加 `_config.yml` 的 `exclude`
  （CLAUDE.md、build.py），推送後確認三個網址 404，講義內容與 repo 逐位元相同。
- 仍會發布的非講義檔：`shell.html`、`home.html`、`package.json`、`package-lock.json`、`check_doi.py`
  （要排除就加進 `_config.yml` 的 `exclude`，先確認學生不需要）。
- 注意：Jekyll 3 的 `exclude` 會取代預設清單；新增不想公開的檔案時記得加進去。

### 清除 git 歷史中的 Drive ID 與帳號（2026/09/26，老師同意改寫歷史＋強制推送）
- 原因：CLAUDE.md 曾寫入存檔區資料夾 ID、week04/papers 資料夾網址、老師公司帳號 email（自 commit `db7700c` 起，共 6 個 commit）。
- 做法：資訊移到 `CLAUDE.local.md`（已 .gitignore）→ `git filter-branch --tree-filter` 以 perl 把 CLAUDE.md 中的
  ID／網址／email 換成「見 CLAUDE.local.md」→ 本機清 refs/original、reflog、`gc --prune=now` → `git push --force-with-lease`。
  本機沒有 git-filter-repo，用 filter-branch 即可（repo 小，數秒完成）。
- 結果：main `4007cae→23064fd`、`claude/dazzling-mayer-eq6w55` `ff0ef6b→5ec002a`、
  `claude/sweet-newton-0eiil5` `039ba59→695740b`、`claude/zealous-tesla-96isa2` `9ade4c3→1ca694a`；
  tag `2026.09.23` 早於存檔區，不含資料，未變動。只有 CLAUDE.md 內容改變，其他檔案與 commit 數相同。
- **強制推送不會觸發 Pages 重建**（線上 CLAUDE.html 仍是舊版），要手動：`gh api -X POST repos/drhhtang-pixel/2026-QDS/pages/builds`。
- 教訓：**Drive ID、網址、帳號 email 等識別資訊一律只寫在 CLAUDE.local.md**；推送前用
  `git grep -e <ID> -e ditldesignfirm` 確認沒有外洩。
- 後續（需老師處理，尚未完成）：
  1. GitHub 仍可用完整 SHA 看到舊 commit（如 `db7700c…`），要徹底移除需向 GitHub Support 申請「Remove sensitive data」。
  2. 還在使用舊 `claude/…` 分支的雲端 session 要結束或重新 clone，否則推送會把舊紀錄帶回來。
  3. 改寫前的本機備份在該 session 的 scratchpad `backup-before-rewrite.git`（含舊資料，/private/tmp 下，確認無誤後可刪）。

## 技術限制與慣例

- 每個 weekNN/index.html 必須是**單一自足檔案**，外部資源只用：`cdnjs.cloudflare.com`（腳本）、Google Fonts
  （Tailwind 已改為建置時編譯內嵌，產物不再用 `cdn.tailwindcss.com`；講義原始檔仍可照舊寫 CDN 標籤）。不要引入其他 CDN 或遠端圖片（claude.ai artifact 版本的 CSP 會擋）。
- 新講義版型沿用既有風格：Tailwind、Noto Sans TC、slate/indigo 色系、白底卡片、深色漸層頁首。
- 內容用繁體中文；書目依 APA 第 7 版（期刊名與卷號斜體）。
- **中文內文引用英文作者（老師規定，2026/09/26，全站統一）**：用 APA 英文格式與**半形括號**（括號前空一格）。
  兩位作者用「&」：`Rittel & Webber (1973)`、`(Tullis & Wood, 2004)`；三位以上一律 `et al.`：
  `Johansson-Sköldberg et al. (2013)`、`(Tranfield et al., 2003)`。不用「等人」「、」「與」「和」連接人名，也不用全形括號（）。
  （文末完整書目條目仍依 APA 7 列出全部作者：`Mura, M., & Beverland, M. B.`。第三堂分頁 6 是原始上傳檔，以 build.py 補丁修正。）
- **參考文獻 DOI（老師規定）**：有 DOI 的書目都加上可點的 `https://doi.org/...` 連結，並逐一確認存在（doi.org handle API／Crossref）；沒有 DOI 的維持純文字。
- 測試：`.claude/launch.json` 有 `site` 設定（`python3 -m http.server 8765`），可用內建瀏覽器開
  `http://localhost:8765/` 檢查目錄頁與 `/week03/`，逐一點 `#tab0`～`#tab6` 確認 iframe 載入、無 JS 錯誤。
  （本機沒有安裝 Playwright；file:// 會被擋，請用本機伺服器。瀏覽器可能快取舊檔，網址加 `?v=N` 強制重新載入。）
