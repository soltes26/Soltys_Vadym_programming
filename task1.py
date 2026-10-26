import sys
from pathlib import Path

NAME = "Vadym"
SURNAME = "Soltys"
GROUP = "IT-32"


USAGE = "usage: python3 task1.py <path> [<path> ...]"


def check_file(path):
    """Повертає (кількість рядків, перший рядок) або кидає виняток."""
    if Path(path).is_dir():
        raise IsADirectoryError(path)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.strip():
        raise ValueError("file is empty")
    lines = text.splitlines()
    return len(lines), lines[0]


def explain(exc):
    """Причина помилки людською мовою."""
    if isinstance(exc, FileNotFoundError):
        return "file not found"
    if isinstance(exc, IsADirectoryError):
        return "is a directory"
    if isinstance(exc, PermissionError):
        return "permission denied"
    if isinstance(exc, UnicodeDecodeError):
        return "not a UTF-8 text file"
    if isinstance(exc, ValueError):
        return str(exc)
    return f"cannot read ({exc.strerror})"

def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    paths = sys.argv[1:]
    if not paths:
        print(USAGE, file=sys.stderr)
        return 2

    failed = 0
    for path in paths:
        try:
            count, first = check_file(path)
        except (OSError, ValueError) as exc:
            failed += 1
            print(f"error: {path}: {explain(exc)} ({type(exc).__name__})",
                  file=sys.stderr)
        else:
            print(f"ok:    {path}: {count} lines, first: {first}")
    print(f"checked {len(paths)}, failed {failed}")
    return 1 if failed else 0


sys.exit(main())
