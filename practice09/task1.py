print("Vadym Soltys, IT-32")

d = 27
c = 6

count = 0
total_sum = 0
product = 1
even_count = 0
odd_count = 0
numbers_line = []

for number in range(d, 32):
    numbers_line.append(str(number))
    count += 1
    total_sum += number
    product *= number
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Numbers from {d} to 31: " + " ".join(numbers_line))
print(f"Count: {count}")
print(f"Sum: {total_sum}")
print(f"Product: {product}")
average = total_sum / count
print(f"Average: {average:.2f}")
print(f"Even: {even_count}, odd: {odd_count}")

print("# while version")
number = d
count_w = 0
sum_w = 0
product_w = 1
even_w = 0
odd_w = 0
numbers_line_w = []

while number <= 31:
    numbers_line_w.append(str(number))
    count_w += 1
    sum_w += number
    product_w *= number
    if number % 2 == 0:
        even_w += 1
    else:
        odd_w += 1
    number += 1

print(f"Numbers from {d} to 31: " + " ".join(numbers_line_w))
print(f"Count: {count_w}")
print(f"Sum: {sum_w}")
print(f"Product: {product_w}")
average_w = sum_w / count_w
print(f"Average: {average_w:.2f}")
print(f"Even: {even_w}, odd: {odd_w}")

countdown_numbers = []
for number in range(c, 0, -1):
    countdown_numbers.append(str(number))
print("Countdown: " + " ".join(countdown_numbers))