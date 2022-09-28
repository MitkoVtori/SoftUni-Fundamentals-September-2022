list_numbers = input().split(' ')
rounded_numbers = [round(float(numbers)) for numbers in list_numbers]
print(rounded_numbers)


# On one line:
print(list(map(lambda x: round(float(x)), input().split(" "))))


# Other way to solve it:

# list_numbers = input().split(' ')
# rounded_numbers = []
#
# for numbers in list_numbers:
#     rounded_numbers.append(round(float(numbers)))
#
# print(rounded_numbers)