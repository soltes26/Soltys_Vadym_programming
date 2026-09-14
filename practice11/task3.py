print("Vadym Soltys, IT-32")

name = "Vadym"
surname = "Soltys"


def get_initials(name: str, surname: str) -> str:
    return f"{name[0]}.{surname[0]}."


def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""
    count = 0
    for char in text.lower():
        if char == letter.lower():
            count += 1
    return count


def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


def reverse_text(text: str) -> str:
    result = ""
    for char in text:
        result = char + result
    return result


full_name = f"{name} {surname}"
initials = get_initials(name, surname)

print(f"Full name: {full_name}")
print(f"Initials: {initials}")

c = len(surname)
vowels_count = count_vowels(surname)
consonants_count = c - vowels_count

print(f"Letters in surname: {c}")
print(f"Vowels: {vowels_count}, consonants: {consonants_count}")

for vowel in "aeiou":
    print(f"{vowel}: {count_letters(surname, letter=vowel)}")

print(f"Default letter 'a': {count_letters(surname)}")

print(f"Reversed surname: {reverse_text(surname)}")

print(f"Docstring: {count_letters.__doc__}")
print(f"Annotations: {count_letters.__annotations__}")