import math
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

NAME = "Vadym"
SURNAME = "Soltys"
GROUP = "IT-32"

BASE = Path(__file__).resolve().parent
SHOWN = os.environ.get("EXPENSES_FILE", "data/expenses.csv")
DATA_FILE = BASE / SHOWN
REPORT_FILE = BASE / "reports" / "expenses_report.txt"
HEADER = "# date;category;amount;note"
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")

USAGE = (
    "usage: python3 task3.py add <date> <category> <amount> <note>\n"
    "       python3 task3.py list\n"
    "       python3 task3.py report"
)


def usage_error(message=None):
    if message:
        print(f"error: {message}", file=sys.stderr)
    print(USAGE, file=sys.stderr)
    return 2

def parse_expense(day, category, amount_text, note):
    """Повертає словник або кидає ValueError з причиною."""
    try:
        if not DATE_RE.fullmatch(day):
            raise ValueError
        datetime.strptime(day, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"bad date {day!r}") from None
    if not category or ";" in category:
        raise ValueError(f"bad category {category!r}")
    try:
        amount = float(amount_text)
        if not math.isfinite(amount):
            raise ValueError
    except ValueError:
        raise ValueError(f"bad amount {amount_text!r}") from None
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount:.2f}")
    return {"date": day, "category": category, "amount": amount, "note": note}

def load_expenses():
    """(список записів, список пропущених (номер рядка, причина))."""
    if DATA_FILE.is_dir():
        raise IsADirectoryError(SHOWN)
    items, skipped = [], []
    with open(DATA_FILE, encoding="utf-8-sig") as f:

        for number, raw in enumerate(f, 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(";", 3)
            try:
                if len(parts) != 4:
                    raise ValueError(f"expected 4 fields, got {len(parts)}")
                items.append(parse_expense(*parts))
            except ValueError as exc:
                skipped.append((number, str(exc)))
    return items, skipped


def report_skipped(skipped):
    if skipped:
        print(f"skipped {len(skipped)} bad line(s):", file=sys.stderr)
        for number, reason in skipped:
            print(f"  line {number}: {reason}", file=sys.stderr)

def cmd_add(args):
    if len(args) < 4:
        return usage_error("add needs date, category, amount and note")
    note = " ".join(args[3:])
    try:
        record = parse_expense(args[0], args[1], args[2], note)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        print("nothing was added", file=sys.stderr)
        return 1

    if DATA_FILE.is_dir():
        raise IsADirectoryError(SHOWN)
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    new_file = not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0
    if not new_file:

        with open(DATA_FILE, encoding="utf-8-sig") as f:
            f.readline()
        with open(DATA_FILE, "rb") as f:
            f.seek(-1, 2)
            missing_newline = f.read(1) != b"\n"
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        if new_file:
            f.write(HEADER + "\n")
        elif missing_newline:
            f.write("\n")
        f.write(f"{record['date']};{record['category']};"
                f"{record['amount']:.2f};{record['note']}\n")
    print(f"added: {record['date']} {record['category']} "
          f"{record['amount']:.2f} ({record['note']})")
    return 0


def cmd_list(args):
    items, skipped = load_expenses()
    print(f"{'date':<10}  {'category':<12} {'amount':>8}  note")
    for e in items:
        print(f"{e['date']:<10}  {e['category']:<12} {e['amount']:>8.2f}  {e['note']}")
    total = sum(e["amount"] for e in items)
    print(f"{len(items)} records, total {total:.2f}")
    report_skipped(skipped)
    return 0


def build_report(items):
    total = sum(e["amount"] for e in items)
    dates = sorted(e["date"] for e in items)
    by_cat, by_day = {}, {}
    for e in items:
        cnt, s = by_cat.get(e["category"], (0, 0.0))
        by_cat[e["category"]] = (cnt + 1, s + e["amount"])
        by_day[e["date"]] = by_day.get(e["date"], 0.0) + e["amount"]
    rows = sorted(by_cat.items(), key=lambda kv: kv[1][1], reverse=True)
    top_day = max(by_day, key=by_day.get)
    priciest = max(items, key=lambda e: e["amount"])
    days = (date.fromisoformat(dates[-1]) - date.fromisoformat(dates[0])).days + 1

    line = "-" * 52
    out = [
        f"Expenses report for {NAME} {SURNAME} ({GROUP})",
        f"Period: {dates[0]} .. {dates[-1]}",
        f"Records: {len(items)}",
        "",
        f"{'category':<10} {'count':>5} {'total':>9} {'share':>7}  chart",
        line,
    ]
    for cat, (cnt, s) in rows:
        share = s / total * 100
        out.append(f"{cat:<10} {cnt:>5} {s:>9.2f} {share:>6.1f}%  {'#' * int(share // 5)}")
    out += [
        line,
        f"{'total':<10} {len(items):>5} {total:>9.2f} {100:>6.1f}%",
        "",
        f"Top day: {top_day} ({by_day[top_day]:.2f})",
        f"Most expensive: {priciest['category']} {priciest['amount']:.2f} ({priciest['note']})",
        f"Average per day: {total / days:.2f}",
    ]
    return "\n".join(out)


def cmd_report(args):
    items, skipped = load_expenses()
    if not items:
        print("error: nothing to report, no valid records", file=sys.stderr)
        report_skipped(skipped)
        return 1
    text = build_report(items)
    REPORT_FILE.parent.mkdir(exist_ok=True)
    REPORT_FILE.write_text(text + "\n", encoding="utf-8")
    print(text)
    print()
    print(f"report saved to: {REPORT_FILE.relative_to(BASE).as_posix()}")
    report_skipped(skipped)
    return 0


COMMANDS = {"add": cmd_add, "list": cmd_list, "report": cmd_report}


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    args = sys.argv[1:]
    if not args:
        return usage_error()
    handler = COMMANDS.get(args[0])
    if handler is None:
        return usage_error(f"unknown command {args[0]}")
    try:
        return handler(args[1:])
    except FileNotFoundError:
        print(f"error: {SHOWN} not found", file=sys.stderr)
    except IsADirectoryError:
        print(f"error: {SHOWN} is a directory, not a file", file=sys.stderr)
    except PermissionError:
        print(f"error: no permission to access {SHOWN}", file=sys.stderr)
    except UnicodeDecodeError:
        print(f"error: {SHOWN} is not a UTF-8 text file", file=sys.stderr)
    except OSError as exc:
        print(f"error: cannot access {SHOWN} ({exc.strerror})", file=sys.stderr)
    return 1


sys.exit(main())
