import os
import sys
from pathlib import Path

NAME = "Vadym"
SURNAME = "Soltys"
GROUP = "IT-32"

USAGE = "usage: python3 task2.py [--force] <source> <destination>"


def error(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def copy_file(source, destination, force):
    src, dst = Path(source), Path(destination)

    if src.is_dir():
        return error(f"source {source} is a directory, not a file")
    try:
        with open(src, encoding="utf-8", newline="") as f:
            text = f.read()
    except FileNotFoundError:
        return error(f"source {source} not found")
    except PermissionError:
        return error(f"no permission to read {source}")
    except UnicodeDecodeError:
        return error(f"source {source} is not a UTF-8 text file")

    if dst.is_dir():
        return error(f"destination {destination} is a directory, not a file")
    if dst.exists() and os.path.samefile(src, dst):
        return error("source and destination are the same file")

    mode = "w" if force else "x"
    try:
        with open(dst, mode, encoding="utf-8", newline="") as f:
            f.write(text)
    except FileExistsError:
        return error(f"{destination} already exists, use --force to overwrite")
    except FileNotFoundError:
        return error(f"destination folder {dst.parent} not found")
    except PermissionError:
        return error(f"no permission to write {destination}")
    except OSError as exc:
        return error(f"cannot write {destination} ({exc.strerror})")

    print(f"copied: {source} -> {destination}")
    return 0


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    args = sys.argv[1:]
    force = "--force" in args
    rest = [a for a in args if a != "--force"]
    if len(rest) != 2 or any(a.startswith("--") for a in rest):
        print(USAGE, file=sys.stderr)
        return 2
    return copy_file(rest[0], rest[1], force)


sys.exit(main())
