def calculations(a, b):
    if command == "subtract":
        result = a - b
    elif command == "add":
        result = a + b
    elif command == "divide":
        result = a / b
    elif command == "multiply":
        result = a * b
    else:
        result = "I don't understand"

    return result


command = input()
first_number = int(input())
second_number = int(input())
calculations = calculations(first_number, second_number)
print(f"{calculations:.0f}")