def make_subjects():
    """Предмети семестру: (title, pairs, grade)."""
    return [
        ("Programming", 3, 11),
        ("Webrozrobka", 2, 9),
        ("Databases", 2, 10),
        ("Math", 1, 10),
        ("English", 2, 12),
    ]


def print_header(name, surname, group):
    print(f"{name} {surname}, {group}")


def print_table(subjects):
    print(f"{'#':<3}{'Subject':<15}{'Pairs':>5}{'Grade':>7}")
    for i, (title, pairs, grade) in enumerate(subjects, 1):
        print(f"{i:<3}{title:<15}{pairs:>5}{grade:>7}")


def total_pairs(subjects):
    total = 0
    for _, pairs, _ in subjects:
        total += pairs
    return total


def most_pairs(subjects):
    best = subjects[0]
    for subject in subjects:
        if subject[1] > best[1]:
            best = subject
    return best


def weakest(subjects):
    worst = subjects[0]
    for subject in subjects:
        if subject[2] < worst[2]:
            worst = subject
    return worst


def get_titles(subjects):
    titles = []
    for title, _, _ in subjects:
        titles.append(title)
    return titles


def get_grades(subjects):
    grades = []
    for _, _, grade in subjects:
        grades.append(grade)
    return grades


def average(values):
    return sum(values) / len(values)


def titles_with_grade(subjects, min_grade):
    result = []
    for title, _, grade in subjects:
        if grade >= min_grade:
            result.append(title)
    return result


def print_histogram(subjects):
    for title, _, grade in subjects:
        print(f"{title}: {'#' * grade}")


def retake(subjects):
    """Перездача предмета з найнижчою оцінкою: +2 бали, але не більше 12."""
    worst = weakest(subjects)
    index = subjects.index(worst)
    title, pairs, grade = worst
    new_grade = min(grade + 2, 12)
    subjects[index] = (title, pairs, new_grade)  # кортеж незмінний - замінюємо цілий
    print(f"Retake: {title} {grade} -> {new_grade}")


def main():
    name = "Vadym"
    surname = "Soltys"
    group = "IT-32"
    subjects = make_subjects()

    print_header(name, surname, group)
    print_table(subjects)
    print("Pairs per week:", total_pairs(subjects))

    top = most_pairs(subjects)
    print(f"Most pairs: {top[0]} ({top[1]})")
    low = weakest(subjects)
    print(f"Weakest subject: {low[0]} ({low[2]})")

    grades = get_grades(subjects)
    print("Titles:", get_titles(subjects))
    print(f"Grades: {grades}, average: {average(grades):.2f}")
    print("Grade 10+:", titles_with_grade(subjects, 10))

    print_histogram(subjects)

    retake(subjects)
    print("Subjects:", subjects)


main()