def read_grade(prompt):
    """Ask for a grade until a valid integer 0-100 is entered."""
    while True:
        text = input(prompt)
        if not text.lstrip("-").isdigit():
            print("Error: digits only")
            continue
        grade = int(text)
        if grade < 0 or grade > 100:
            print("Error: the value must be between 0 and 100")
            continue
        return grade


def to_letter(grade):
    """Convert a numeric grade to a letter grade A-F."""
    if grade >= 90:
        return "A"
    if grade >= 82:
        return "B"
    if grade >= 74:
        return "C"
    if grade >= 64:
        return "D"
    if grade >= 60:
        return "E"
    return "F"


def average(grades):
    """Return the arithmetic mean of a list of grades."""
    return sum(grades) / len(grades)


def count_above(grades, limit):
    """Return how many grades are greater than limit."""
    count = 0
    for grade in grades:
        if grade > limit:
            count += 1
    return count


def print_report(name, group, grades):
    """Print a full report about the student's grades."""
    avg = average(grades)
    letter = to_letter(avg)
    best = max(grades)
    worst = min(grades)
    above_avg = count_above(grades, avg)

    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    print("Grades: " + " ".join(str(g) for g in grades))
    print(f"Average: {avg:.2f} -> {letter}")
    print(f"Best: {best}, worst: {worst}")
    print(f"Above average: {above_avg}")


def main():
    """Entry point: collect grades and print the report."""
    print("Vadym Soltys, IT-32")

    name = "Vadym Soltys"
    group = "IT-32"
    n = 5

    grades = []
    for i in range(1, n + 1):
        grade = read_grade(f"Grade {i} (0-100): ")
        grades.append(grade)

    print_report(name, group, grades)


main()