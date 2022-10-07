def factorial_number(first_number, second_number):
    for factorial in range(1, first_number):
        first_number *= factorial

    for factorial_second in range(1, second_number):
        second_number *= factorial_second

    result = first_number / second_number

    return f"{result:.2f}"


first_num = int(input())
second_num = int(input())
print(factorial_number(first_num, second_num))
