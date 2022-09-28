numbers_list = list(map(float, input().split(' ')))
absolute_value_list = [abs(numbers) for numbers in numbers_list]
print(absolute_value_list)