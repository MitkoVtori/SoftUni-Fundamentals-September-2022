numbers = input()
odd_sum = 0
even_sum = 0

for index in range(len(numbers)):
    current_number = int(numbers[index])
    if current_number % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')