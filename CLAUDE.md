# 2026 QDS 課程講義網站

## 專案概述

這是 Qualitative Design Studies（QDS 2026，授課：唐玄輝 Hsien-Hui TANG，drhhtang）的課程講義網站。
目前收錄**第三堂課**的 7 份講義，以分頁（tab）方式呈現，給修課學生瀏覽。

- 使用者：授課老師本人（olddrhhtang）。溝通語言：**繁體中文**（偶爾用英文下指令）。
- 讀者：研究所學生，會用電腦與手機瀏覽。
- 發布方式：GitHub Pages（此資料夾即 repository 根目錄，`index.html` 為首頁）。
  另有一份 claude.ai 上的 artifact 版本：https://claude.ai/artifact/ENDbtkShVQv5TY8SW2iusV
  （Claude Code 無法更新該 artifact，以 GitHub Pages 為主要發布管道。）

## 檔案結構

```
2026 QDS/
├── CLAUDE.md        ← 本文件
├── build.py         ← 建置腳本：讀 sources/ + shell.html，產生 index.html
├── shell.html       ← 外框頁（分頁列、上一份/下一份、頁尾更新日期與更新紀錄）
├── index.html       ← 建置產物，單一自足檔案（約 2.4 MB），不要手動編輯
└── sources/         ← 各份講義原始檔
    ├── The_Secrets_of_Critical_Form_for_Reading_Papers.html   (打包格式，見下方)
    ├── apa.html
    ├── apa_bias_free.html   (APA「無偏見語言指引」說明面板，build.py 插入 apa.html；可直接編輯)
    ├── Google_Scholar_vs_Scopus_vs_WoS_vs_SDOL.html
    ├── AI質化研究工具與平台全覽指南.html
    ├── Natural_Intelligence_in_Design_answer.html
    ├── natural_intelligence_design_AI.html
    └── business_db.html   (由 Claude 撰寫的新講義，可直接編輯)
```

## 建置

```bash
python3 build.py      # 只用 Python 標準函式庫，產生 index.html
```

**每次修改後都要重新執行 build.py**，再檢查 index.html。

## 分頁（依上課講述順序，不可任意調換）

| # | 分頁名稱 | 來源檔 |
|---|---|---|
| 1 | Critical Form 閱讀論文的秘訣 | The_Secrets_of_Critical_Form_for_Reading_Papers.html |
| 2 | APA 第七版格式指南 | apa.html |
| 3 | 學術資料庫比較 | Google_Scholar_vs_Scopus_vs_WoS_vs_SDOL.html |
| 4 | AI 質化研究工具 | AI質化研究工具與平台全覽指南.html |
| 5 | Natural Intelligence 解答 by drhhtang | Natural_Intelligence_in_Design_answer.html |
| 6 | Natural Intelligence 解答 by AI | natural_intelligence_design_AI.html |
| 7 | 商學院學術資料庫 | business_db.html |

分頁名稱與順序定義在 `build.py` 的 `docs` / `files` 清單中。

## 架構重點（build.py 在做什麼）

1. **第 1 份講義是「打包格式」**（`__bundler/manifest` + `__bundler/template`，資源以 gzip+base64 存放，
   執行時轉成 blob URL）。發布環境會擋 blob 腳本，所以 build.py 會把它**拆解還原**成一般 HTML：
   Tailwind 改用 `https://cdn.tailwindcss.com`，Font Awesome 的 CSS 與字型取出重用。
2. **Font Awesome 內嵌**：其他講義原本從 cdnjs 載入 FA 的 CSS，build.py 把該 `<link>` 換成標記
   `<!--FA_INLINE-->`，外框頁在執行時再注入一份共用的 FA CSS（字型以 woff2 data URI 內嵌，只存一份）。
3. **每份講義放在各自的 iframe（srcdoc）**，樣式與腳本互不干擾；iframe 在第一次點選時才建立。
4. **內容修正以「字串替換補丁」寫在 build.py 裡**，原始檔保持不動。每個補丁都有 `assert` 確認
   目標字串恰好出現預期次數，原始檔若被換掉會立刻報錯，不會默默失效。
   - 對原始上傳檔（第 1～6 份）：沿用補丁方式，或在老師同意後直接改 sources/ 檔案，二選一並保持一致。
   - business_db.html：可直接編輯。
5. 所有講義資料以 JSON 放在 `<script id="data" type="application/json">`，`</` 會被跳脫成 `<\/`
   （所以在 index.html 裡用 grep 搜尋 `</em>` 會找不到，要搜 `<\/em>`）。

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
- 分頁 2：「提倡包容性與多元語言」卡片加「了解更多：無偏見語言指引」按鈕，開啟頁內說明面板（內容在 `sources/apa_bias_free.html`）。

## 更新紀錄規則（重要）

老師要求：**網頁最下方顯示每次更新日期，各分頁依自己的更新狀況，不必一致。**

每次修改某一分頁時，在 `build.py` 的 `LOG` 對應位置**附加**一筆 `('YYYY/MM/DD', '修改說明')`，
只改被修改的那一頁；新增分頁時同步新增一個 LOG 項目（有 `assert len(LOG)==len(docs)` 檢查）。
日期格式：`2026/09/23`。說明用繁體中文、簡短。

## 待決事項 / 建議（尚未執行，需老師同意）

- 未來加入第四堂以後的課：可在同一 repository 新增 `lesson4.html`（複製 build 流程），
  或把 `index.html` 改成各堂課目錄頁。

## 發布到 GitHub Pages

- Repository：https://github.com/drhhtang-pixel/2026-QDS（public，帳號 drhhtang-pixel）
- 網址：https://drhhtang-pixel.github.io/2026-QDS/
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

- index.html 必須是**單一自足檔案**，外部資源只用：`cdn.tailwindcss.com`、`cdnjs.cloudflare.com`（腳本）、
  Google Fonts。不要引入其他 CDN 或遠端圖片（claude.ai artifact 版本的 CSP 會擋）。
- 新講義版型沿用既有風格：Tailwind、Noto Sans TC、slate/indigo 色系、白底卡片、深色漸層頁首。
- 內容用繁體中文；書目依 APA 第 7 版（期刊名與卷號斜體）。
- 測試：可用 Playwright 開啟 index.html，逐一點 `#tab0`～`#tab6`，確認 iframe 內容載入、無 JS 錯誤。
