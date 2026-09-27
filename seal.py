"""把尚未公開的講義原始檔加密成 sealed/sources.tar.gz.enc（可以安全地推上公開 repo）。

老師規定（2026/09/27）：課前準備在上課前 7 天 07:00 公開、講義在上課當天 07:00 公開。
公開 repo 裡只要出現明文原始檔就等於公開，所以未公開的 sources/weekNN/ 列在 .gitignore，
改用這個腳本加密後推送；GitHub Actions（release.yml）用 secrets.QDS_SEAL_KEY 解開、依時間建置。

用法：python3 seal.py          修改任何未公開講義後都要重新執行，再 commit sealed/ 並推送
密鑰：private/seal.key（.gitignore 排除，只在老師的 Mac）；GitHub 上存在 repository secret QDS_SEAL_KEY。
"""
import subprocess,tarfile,io,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
KEY=ROOT/'private'/'seal.key'
OUT=ROOT/'sealed'/'sources.tar.gz.enc'

def ignored(p):
    return subprocess.run(['git','check-ignore','-q',str(p)],cwd=ROOT).returncode==0

dirs=sorted(d for d in (ROOT/'sources').glob('week*') if d.is_dir() and ignored(d))
if not dirs: sys.exit('沒有需要加密的未公開講義（sources/weekNN/ 都沒有被 .gitignore 排除）')
if not KEY.exists(): sys.exit('找不到 %s'%KEY)

buf=io.BytesIO()
with tarfile.open(fileobj=buf,mode='w:gz') as tar:
    for d in dirs:
        for f in sorted(d.rglob('*')):
            if f.is_file() and f.name!='.DS_Store':
                ti=tar.gettarinfo(str(f),arcname=str(f.relative_to(ROOT)))
                ti.uid=ti.gid=0; ti.uname=ti.gname=''; ti.mtime=0
                with open(f,'rb') as fh: tar.addfile(ti,fh)
OUT.parent.mkdir(exist_ok=True)
env=dict(os.environ,QDS_SEAL_KEY=KEY.read_text().strip())
r=subprocess.run(['openssl','enc','-aes-256-cbc','-pbkdf2','-iter','200000','-md','sha256','-salt',
                  '-pass','env:QDS_SEAL_KEY','-out',str(OUT)],input=buf.getvalue(),env=env)
if r.returncode: sys.exit('加密失敗')
# 立刻解密驗證
chk=subprocess.run(['openssl','enc','-d','-aes-256-cbc','-pbkdf2','-iter','200000','-md','sha256',
                    '-pass','env:QDS_SEAL_KEY','-in',str(OUT)],capture_output=True,env=env)
assert chk.returncode==0 and chk.stdout==buf.getvalue(),'解密驗證失敗'
print('已加密 %s → %s（%.1f MB）'%('、'.join(d.name for d in dirs),OUT.relative_to(ROOT),OUT.stat().st_size/1e6))
