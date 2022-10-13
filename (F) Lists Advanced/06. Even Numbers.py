list_numbers = list(map(int, input().split(', ')))
even_numbers = [index for index in range(len(list_numbers)) if list_numbers[index] % 2 == 0]
print(even_numbers)


# list_numbers = list(map(int, input().split(', ')))
# print([index for index in range(len(list_numbers)) if list_numbers[index] % 2 == 0])


# numbers = input().split(', ')
# even_numbers = [index for index in range(len(numbers)) if int(numbers[index]) % 2 == 0]
# print(even_numbers)
