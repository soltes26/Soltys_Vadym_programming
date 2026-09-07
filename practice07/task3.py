print("Vadym Soltys, IT-32")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, //, %, **): ").strip()
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result:.4f}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result:.4f}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result:.4f}")
elif operator == "/":
    if num2 == 0:
        print("Error: division by zero is not allowed")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.4f}")
elif operator == "//":
    if num2 == 0:
        print("Error: division by zero is not allowed")
    else:
        result = num1 // num2
        print(f"{num1} // {num2} = {result:.4f}")
elif operator == "%":
    if num2 == 0:
        print("Error: division by zero is not allowed")
    else:
        result = num1 % num2
        print(f"{num1} % {num2} = {result:.4f}")
elif operator == "**":
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result:.4f}")
else:
    print(f"Unknown operator: {operator}")