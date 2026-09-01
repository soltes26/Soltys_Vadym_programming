a = 27  
b = 1    
surname_latin = "Soltys"
c = len(surname_latin)  

print(f"a = {a}, b = {b}, c = {c}")

day_greater_than_month = a > b
day_less_than_letters = a < c
month_greater_equal_letters = b >= c
month_in_valid_range = 1 <= b <= 12  
day_equals_month = a == b
month_not_equal_letters = b != c

print(f"a > b -> {day_greater_than_month}, type: {type(day_greater_than_month)}")
print(f"a < c -> {day_less_than_letters}, type: {type(day_less_than_letters)}")
print(f"b >= c -> {month_greater_equal_letters}, type: {type(month_greater_equal_letters)}")
print(f"1 <= b <= 12 -> {month_in_valid_range}, type: {type(month_in_valid_range)}")
print(f"a == b -> {day_equals_month}, type: {type(day_equals_month)}")
print(f"b != c -> {month_not_equal_letters}, type: {type(month_not_equal_letters)}")