me = {
    "name": "Vadym",
    "surname": "Soltys",
    "group": "IT-32",
    "city": "Lutsk",
    "birth_year": 2009,
    "hobbies": ["video games", "running", "guitar"],
}

print("Усі пари словника:")
for key, value in me.items():
    print(f"{key}: {value}")

print("\nКлючі:", list(me.keys()))
print("Кількість пар:", len(me))

print("\nГрупа:", me["group"])
print("Email:", me.get("email", "unknown"))

me["email"] = "2024.soltys.vadym@ktbp.net.ua"
me["city"] = "Kyiv"
removed = me.pop("birth_year")
print("\nВилучене значення birth_year:", removed)

print("\nСловник після всіх змін:")
print(me)

print("\nЧи є ключ phone:", "phone" in me)