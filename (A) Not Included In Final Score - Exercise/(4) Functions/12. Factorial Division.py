first_number = int(input())
second_number = int(input())

for factorial in range(1, first_number):
    first_number *= factorial

for factorial_second in range(1, second_number):
    second_number *= factorial_second

result = first_number / second_number

print(f"{result:.2f}")