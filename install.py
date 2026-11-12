import argparse,shutil
from pathlib import Path
def main():
    p=argparse.ArgumentParser(description="Install the bundled Codex skill without overwriting")
    p.add_argument("--skills-dir",type=Path,default=Path.home()/".agents"/"skills")
    a=p.parse_args()
    source=Path(__file__).resolve().parent/"skills"/"tencent-fde-industry-practice"
    target=a.skills_dir.expanduser().resolve()/"tencent-fde-industry-practice"
    if not (source/"SKILL.md").is_file():p.exit(1,"Package incomplete: SKILL.md missing\n")
    if target.exists() or target.is_symlink():p.exit(1,"Already exists; no files changed: "+str(target)+"\n")
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copytree(source,target)
    print("Installed: "+str(target))
    print("Start a new Codex chat; restart if the skill does not appear.")
if __name__=="__main__":main()
