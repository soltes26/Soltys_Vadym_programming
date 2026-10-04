about = "I love listening to music and playing video games"
day = 27
my_name = "Vadym"

words = about.split()
print("Кількість слів:", len(words))
print("Найдовше слово:", max(words, key=len))
print("Слова у зворотному порядку:", " ".join(words[::-1]))

print("Літера 'a' трапляється разів:", about.lower().count("a"))

print("Кожне слово з великої:", about.title())
print("Пробіли замінено на _:", about.replace(" ", "_"))


def is_palindrome(text):
    """Паліндром без урахування регістру та пробілів."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


print(f"is_palindrome('{my_name}'):", is_palindrome(my_name))
print("is_palindrome('Never odd or even'):", is_palindrome("Never odd or even"))


def caesar(text, shift):
    """Шифр Цезаря для латинських літер; інші символи не змінюються."""
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


encrypted = caesar(my_name, day)
decrypted = caesar(encrypted, -day)
print(f"Зашифроване імʼя (зсув {day}):", encrypted)
print("Розшифроване назад:", decrypted)