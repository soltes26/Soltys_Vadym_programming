
name = input("Enter your name: ")
age = int(input("Enter your age: "))

in_range = 18 <= age <= 60
is_even = age % 2 == 0
both = in_range and is_even
either = in_range or is_even
years_left = 60 - age

print(f"Hello, {name}!")
print(f"Age {age} is in range [18, 60]: {in_range}")
print(f"Age {age} is even: {is_even}")
print(f"Both conditions true: {both}")
print(f"At least one condition true: {either}")
print(f"Years left until 60: {years_left}")