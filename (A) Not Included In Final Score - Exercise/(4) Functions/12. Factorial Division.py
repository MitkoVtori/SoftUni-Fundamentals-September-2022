def factorial_division(first: int, second: int):
    for factorial in range(1, first):
        first *= factorial
    for factorial in range(1, second):
        second *= factorial
    division = first / second
    return f'{division:.2f}'


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))
