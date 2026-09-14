print("Vadym Soltys, IT-32")

y = 2009


def print_age(year):
    age = 2026 - year
    print(f"Age: {age}")


def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1
    age = current_year - year
    return age
    print("after return")


result = print_age(y)
print(f"print_age returned: {result}")

age_from_function = get_age(y)
print(f"Age from get_age: {age_from_function}")

age_in_months = age_from_function * 12
age_in_weeks = age_from_function * 52

print(f"Age in months: {age_in_months}")
print(f"Age in weeks: {age_in_weeks}")

age_in_2030 = get_age(y, current_year=2030)
print(f"Age in 2030: {age_in_2030}")

invalid_result = get_age(3000)
print(f"Invalid year 3000 gives: {invalid_result}")