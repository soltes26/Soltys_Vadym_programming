from pathlib import Path

NAME = "Vadym"
SURNAME = "Soltys"
GROUP = "IT-32"
YEAR = 2007
LANGUAGE = "Python"

def main():
    script = Path(__file__).resolve()
    base = script.parent

    print(f"cwd:         {Path.cwd()}")
    print(f"script:      {script}")
    print(f"script dir:  {base}")
    print(f"home:        {Path.home()}")
    
    for folder in ("data", "reports", "backups"):
        (base / folder).mkdir(exist_ok=True)

    profile = base / "data" / "profile.txt"
    profile.write_text(
        f"name: {NAME}\nsurname: {SURNAME}\ngroup: {GROUP}\n"
        f"year: {YEAR}\nlanguage: {LANGUAGE}\n",
        encoding="utf-8",
    )

    print()
    print(f"profile path: {profile}")
    print(f"relative:    {profile.relative_to(base)}")
    print(f"name:        {profile.name}")
    print(f"stem:        {profile.stem}")
    print(f"suffix:      {profile.suffix}")
    print(f"parent:      {profile.parent.name}")
    print(f"size:        {profile.stat().st_size} bytes")

    print()
    print("project tree:")
    for folder in sorted(p for p in base.iterdir() if p.is_dir()):
        print(f"  {folder.name}/")
        for file in sorted(p for p in folder.iterdir() if p.is_file()):
            print(f"    {file.name}")


main()
