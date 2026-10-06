from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

NAME = "Vadym"
SURNAME = "Soltys"

RUNS_FILE = Path(__file__).resolve().parent / "data" / "runs.log"


def read_lines(path):
    """Непорожні рядки файлу (або [] якщо файлу немає)."""
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def count_runs(path):
    return len(read_lines(path))


def add_run(path, number):
    path.parent.mkdir(exist_ok=True)
    stamp = datetime.now(ZoneInfo("Europe/Kyiv")).strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{number};{stamp};{NAME} {SURNAME}\n")


def show_history(path, last=3):
    records = [line.split(";") for line in read_lines(path)]
    print(f"runs so far: {len(records)}")
    print("last runs:")
    for num, stamp, who in records[-last:]:
        print(f"  #{num:>2}  {stamp}  {who}")
    print(f"first run was at {records[0][1]}")


def main():
    previous = count_runs(RUNS_FILE)
    number = previous + 1
    if previous == 0:
        print(f"file {RUNS_FILE.name} was just created")
    add_run(RUNS_FILE, number)
    print(f"Hello, {NAME} {SURNAME}! This is run number {number}.")
    show_history(RUNS_FILE)


main()
