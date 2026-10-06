import sys
from datetime import date
from pathlib import Path

NAME = "Vadym"
SURNAME = "Soltys"
GROUP = "IT-32"

BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "data" / "expenses.csv"
REPORT_FILE = BASE / "reports" / "expenses_report.txt"
HEADER = "# date;category;amount;note"

USAGE = (
    "usage: python3 task3.py add <date> <category> <amount> <note>\n"
    "       python3 task3.py list\n"
    "       python3 task3.py report"
)


def fail(message=None):
    if message:
        print(f"error: {message}")
    print(USAGE)


def add_expense(args):
    if len(args) < 4:
        fail("add needs date, category, amount and note")
        return
    day, category, amount_text = args[0], args[1], args[2]
    note = " ".join(args[3:])
    try:
        date.fromisoformat(day)
        amount = float(amount_text)
    except ValueError:
        fail("date must be YYYY-MM-DD and amount must be a number")
        return
    DATA_FILE.parent.mkdir(exist_ok=True)
    new_file = not DATA_FILE.exists()
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        if new_file:
            f.write(HEADER + "\n")
        f.write(f"{day};{category};{amount:.2f};{note}\n")
    print(f"added: {day} {category} {amount:.2f} ({note})")


def load_expenses():
    """Список словників; порожні рядки та коментарі (#) пропускаємо."""
    items = []
    if not DATA_FILE.exists():
        return items
    with open(DATA_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(";", 3)
            if len(parts) < 4:
                continue
            items.append({"date": parts[0], "category": parts[1],
                          "amount": float(parts[2]), "note": parts[3]})
    return items


def list_expenses():
    items = load_expenses()
    print(f"{'date':<10}  {'category':<12} {'amount':>8}  note")
    for e in items:
        print(f"{e['date']:<10}  {e['category']:<12} {e['amount']:>8.2f}  {e['note']}")
    total = sum(e["amount"] for e in items)
    print(f"{len(items)} records, total {total:.2f}")


def build_report(items):
    total = sum(e["amount"] for e in items)
    dates = sorted(e["date"] for e in items)
    by_cat = {}
    for e in items:
        cnt, s = by_cat.get(e["category"], (0, 0.0))
        by_cat[e["category"]] = (cnt + 1, s + e["amount"])
    rows = sorted(by_cat.items(), key=lambda kv: kv[1][1], reverse=True)

    by_day = {}
    for e in items:
        by_day[e["date"]] = by_day.get(e["date"], 0.0) + e["amount"]
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


def report():
    items = load_expenses()
    if not items:
        print("error: no expenses yet, use the add command first")
        return
    text = build_report(items)
    REPORT_FILE.parent.mkdir(exist_ok=True)
    REPORT_FILE.write_text(text + "\n", encoding="utf-8")
    print(text)
    print()
    print(f"report saved to: {REPORT_FILE.relative_to(BASE)}")


def main():
    args = sys.argv[1:]
    if not args:
        print(USAGE)
        return
    command, rest = args[0], args[1:]
    if command == "add":
        add_expense(rest)
    elif command == "list":
        list_expenses()
    elif command == "report":
        report()
    else:
        fail(f"unknown command {command}")


main()
