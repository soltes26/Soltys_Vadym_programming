print("Vadym Soltys, IT-32")

number = int(input("Enter an integer: "))

if number <= 0:
    print("Number must be positive")
else:
    digits_count = 0
    digits_sum = 0
    max_digit = 0
    min_digit = 9
    reversed_number = 0

    while number > 0:
        digit = number % 10
        digits_count += 1
        digits_sum += digit
        if digit > max_digit:
            max_digit = digit
        if digit < min_digit:
            min_digit = digit
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    print(f"Digits: {digits_count}")
    print(f"Sum of digits: {digits_sum}")
    print(f"Max digit: {max_digit}, min digit: {min_digit}")
    print(f"Reversed: {reversed_number}")