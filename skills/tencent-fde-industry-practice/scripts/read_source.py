"""Read a bounded line range from the owner's matching local OCR source. Read-only."""
import argparse,hashlib,json,os,re,sys
from pathlib import Path
for stream in (sys.stdout,sys.stderr):
    try:stream.reconfigure(encoding='utf-8')
    except (AttributeError,ValueError):pass
base=Path(__file__).resolve().parents[1]
manifest=json.loads((base/'references/source-manifest.json').read_text(encoding='utf-8'))
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--source',type=Path,help='Your local OCR Markdown; overrides the recorded path')
p.add_argument('--chapter',type=int)
p.add_argument('--start',type=int)
p.add_argument('--end',type=int)
p.add_argument('--find',help='Literal case-insensitive keyword')
p.add_argument('--limit',type=int,default=60)
a=p.parse_args()
if not 1<=a.limit<=100:p.error('--limit must be between 1 and 100')
choice=a.source or os.getenv(manifest['source_env']) or manifest.get('source_path')
if not choice:sys.exit('未配置原文；可使用章节学习，原句核验请指定 --source。')
path=Path(choice).expanduser()
if not path.is_file():sys.exit('原文文件不存在；请用 --source 指定本地文件。')
data=path.read_bytes()
if hashlib.sha256(data).hexdigest()!=manifest['sha256']:sys.exit('SHA-256不符：不能沿用此版本的行号或引文。')
lines=data.decode('utf-8-sig').splitlines()
def safe(s):
    s=re.sub(r'<img\b[^>]*>', '[图片：OCR未识别视觉内容]', s,flags=re.I)
    s=re.sub(r'https?://\S*authorization=\S+','[临时图片链接已省略]',s)
    return s
if a.find:
    matches=[(n,s) for n,s in enumerate(lines,1) if a.find.casefold() in s.casefold()]
    for n,s in matches[:a.limit]:
        at=s.casefold().find(a.find.casefold())
        print(f'{n}: {safe(s[max(0,at-60):at+180])}')
    print(f'匹配{len(matches)}行，显示{min(a.limit,len(matches))}行。')
else:
    ch=next((x for x in manifest['chapters'] if x['number']==a.chapter),None)
    if a.chapter and not ch:p.error('chapter not found')
    start=a.start if a.start is not None else ch['start_line'] if ch else 1
    requested=a.end if a.end is not None else ch['end_line'] if ch else len(lines)
    if start<1 or requested<start or requested>len(lines):p.error('invalid line range')
    end=min(requested,start+a.limit-1)
    for n in range(start,end+1):print(f'{n}: {safe(lines[n-1])}')
    if end<requested:print(f'继续：--start {end+1} --end {requested}')
