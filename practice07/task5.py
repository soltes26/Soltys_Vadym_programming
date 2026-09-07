print("Vadym Soltys, IT-32")

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

is_valid = True
reason = ""

if month < 1 or month > 12:
    is_valid = False
    reason = f"month {month} is invalid"
elif year <= 0:
    is_valid = False
    reason = f"year {year} is invalid"
else:
    if month in (1, 3, 5, 7, 8, 10, 12):
        max_day = 31
    elif month in (4, 6, 9, 11):
        max_day = 30
    else:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        max_day = 29 if is_leap else 28

    if day < 1 or day > max_day:
        is_valid = False
        reason = f"month {month} has only {max_day} days"

if is_valid:
    print("Date is valid")
else:
    print(f"Date is invalid: {reason}")