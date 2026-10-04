full_name = " sOLTYS   vadym  IVANOVYCH "

clean_name = " ".join(full_name.split()).title()
print("Охайне імʼя:", clean_name)
print("Довжина:", len(clean_name))

surname, name, patronymic = clean_name.split()

print("Перший і останній символ прізвища:", surname[0], surname[-1])
print("Прізвище навпаки:", surname[::-1])
print("Імʼя у форматі:", f"{surname} {name[0]}. {patronymic[0]}.")
print("Ініціали:", surname[0] + name[0] + patronymic[0])

vowels = "aeiouy"
vowel_count = sum(1 for ch in clean_name.lower() if ch in vowels)
print("Кількість голосних у повному імені:", vowel_count)

group = "IT-32"
dash = group.find("-")
before = group[:dash]
after = group[dash + 1:]
print("Частина до дефіса:", before)
print("Частина після дефіса:", after)
print("Після дефіса число?", after.isdigit())

login = f"{name[0]}.{surname}".lower()
email = f"{login}@student.edu.ua"
print("Логін:", login)
print("Пошта:", email)