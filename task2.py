grades_str = "65, 57, 79, 69"
subjects_str = "Programming, Database, English, Web Development"

grades = [int(x) for x in grades_str.split(", ")]
subjects = subjects_str.split(", ")

print("Оцінки:", grades)
print(f"Середня оцінка: {sum(grades) / len(grades):.2f}")
print("Найвища:", max(grades))
print("Найнижча:", min(grades))
print("Оцінки через ' | ':", " | ".join(str(g) for g in grades))

print("Предмети:", subjects)

print()
print(f"{'№':<4}{'Предмет':<20}{'Оцінка':>8}")
print("-" * 32)
for i, (subject, grade) in enumerate(zip(subjects, grades), start=1):
    print(f"{i:<4}{subject:<20}{grade:>8}")
print()

longest = max(subjects, key=len)
print(f"Найдовша назва: {longest} ({len(longest)} символів)")