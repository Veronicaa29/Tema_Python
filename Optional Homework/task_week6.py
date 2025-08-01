# Custom Calculator Function

def calculate(*numbers, operation='+'):
    if not numbers:
        return 0

    result = numbers[0]

    try:
        for num in numbers[1:]:
            if operation == '+':
                result += num
            elif operation == '-':
                result -= num
            elif operation == '*':
                result *= num
            elif operation == '/':
                if num == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result /= num
            else:
                return "Invalid operation"
        return result
    except ZeroDivisionError as e:
        return f"Error: {e}"

print("Add:", calculate(1, 2, 3)) 
print("Multiply:", calculate(2, 3, 4, operation='*'))
print("Divide with 0:", calculate(10, 0, operation='/'))
print("Subtract with no numbers:", calculate(operation='-'))



# Sort Students by Score Using Lambda

names = ["Lucas", "Nataly", "Megi", "Maria", "Steven"]
scores = [85, 92, 78, 81, 67]

students = list(zip(names, scores))

filtered_sorted = sorted(
    [student for student in students if student[1] >= 80],
    key=lambda x: x[1],
    reverse=True
)

for name, score in filtered_sorted:
    print(f"{name}: {score}")



# Validate Age Input with Exception Handling

def check_age(age_input):
    try:
        if age_input == "":
            raise ValueError("Age input cannot be empty.")

        age = int(age_input)

        if age < 0:
            raise ValueError("Age cannot be negative.")
        if age > 120:
            raise ValueError("Age is unrealistically high.")

        print(f"Age is valid: {age}")

    except ValueError as ve:
        print("Validation error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("Validation complete.")

print("Test 1: Valid age")
check_age("30")

print("\nTest 2: Empty input")
check_age("")

print("\nTest 3: Negative number")
check_age("-5")

print("\nTest 4: Too large number")
check_age("150")

print("\nTest 5: Not a number")
check_age("twenty")