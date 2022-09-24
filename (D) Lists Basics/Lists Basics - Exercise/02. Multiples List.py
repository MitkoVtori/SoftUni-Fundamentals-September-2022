first_number = int(input())
first_number_cnt = first_number
second_number = int(input())
list_numbers = []

for multiply in range(1, second_number + 1):
    list_numbers.append(first_number_cnt)
    # We use the first_number_cnt because for example, if first_number = 2, 
    # and we add first_number to first_number it will become 4, and after that instead of 4 + 2 we'll have 4 + 4 and that gives us wrong information.
    first_number_cnt += first_number

print(list_numbers)
