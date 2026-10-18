# QDS 2026 舊網站轉址（old-site-redirect 分支）

2026/10/18 起，QDS 2026 講義只放在新網站 https://qds.ditldesign.com/ 。
GitHub Pages 改從這個分支發布：舊網址（首頁、第 1–6 週、其他路徑的 404）都會轉到新網站的同一頁，並保留 `#分頁` 位置。

- 講義原始檔與 build.py 仍在 `main` 分支，新網站部署照舊（worktree 的 `deploy.sh --content`）。
- 要恢復舊網站：Settings → Pages 的來源改回 `main`，並重新啟用「定時公開講義」workflow。
