def even_odd_sum(numbers, even, odd):
    for index in range(len(numbers)):
        current_number = int(numbers[index])
        if current_number % 2 == 0:
            even += current_number
        else:
            odd += current_number

    return f'Odd sum = {odd}, Even sum = {even}'


numbers = input()
even_sum = 0
odd_sum = 0
print(even_odd_sum(numbers, even_sum, odd_sum))
