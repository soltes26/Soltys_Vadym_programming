def print_card():
    print("Name: Vadym Soltys")
    print("Group: IT-32")
    print("Birth year: 2009")


def print_card_args(name, surname, group="IT-32", year=2009):
    print(f"{name} {surname}, {group}, {year}")


print("Vadym Soltys, IT-32")

print("--- no parameters, call 1 ---")
print_card()
print("--- no parameters, call 2 ---")
print_card()
print("--- no parameters, call 3 ---")
print_card()

print("--- positional arguments ---")
print_card_args("Vadym", "Soltys", "IT-32", 2009)

print("--- keyword arguments ---")
print_card_args(year=2009, group="IT-32", surname="Soltys", name="Vadym")

print("--- default group ---")
print_card_args("Vadym", "Soltys", year=2009)