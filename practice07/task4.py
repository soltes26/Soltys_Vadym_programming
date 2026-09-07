print("Vadym Soltys, IT-32")

score = int(input("Enter your score (0-100): "))
missed = int(input("Enter number of missed classes: "))

total_classes = 16

if score < 0 or score > 100:
    print("Error: score must be between 0 and 100")
else:
    if score >= 90:
        grade = "A"
    elif score >= 82:
        grade = "B"
    elif score >= 74:
        grade = "C"
    elif score >= 64:
        grade = "D"
    elif score >= 60:
        grade = "E"
    else:
        grade = "F"

    passed = "passed" if grade != "F" else "failed"

    if missed / total_classes > 0.3:
        print("Warning: attendance below 70%, you are not admitted to the exam")

    print(f"Score: {score}, Grade: {grade}, Status: {passed}")