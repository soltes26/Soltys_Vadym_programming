schedule = {
    "Mon": ["Administration", "Programming", "Ukr lang"],
    "Tue": ["Databases", "Programming", "IT law"],
    "Wed": ["Web rozrobka", "English", "Web rozrobka"],
    "Thu": ["Administration", "Programming", "Web rozrobka"],
    "Fri": ["IT law", "English", "Databases"],
}

print(f"{'Day':<5}{'Pairs':<7}Subjects")
for day, subjects in schedule.items():
    print(f"{day:<5}{len(subjects):<7}{', '.join(subjects)}")

total = sum(len(subjects) for subjects in schedule.values())
print("\nЗагальна кількість пар на тиждень:", total)

busiest = max(schedule, key=lambda day: len(schedule[day]))
print("День з найбільшою кількістю пар:", busiest, f"({len(schedule[busiest])})")

all_subjects = set()
for subjects in schedule.values():
    all_subjects.update(subjects)
print("\nУнікальні предмети:", all_subjects)
print("Кількість унікальних предметів:", len(all_subjects))

mon = set(schedule["Mon"])
wed = set(schedule["Wed"])
print("\nІ в понеділок, і в середу:", mon & wed)
print("У понеділок, але не в середу:", mon - wed)

def count_subjects(sched):
    counts = {}
    for subjects in sched.values():
        for subject in subjects:
            counts[subject] = counts.get(subject, 0) + 1
    return counts

counts = count_subjects(schedule)
print("\nКількість пар по предметах:", counts)

ranking = sorted(counts.items(), key=lambda item: item[1], reverse=True)
print("\nРейтинг предметів:")
for place, (subject, number) in enumerate(ranking, start=1):
    print(f"{place}. {subject} — {number}")