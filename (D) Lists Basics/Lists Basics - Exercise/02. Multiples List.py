first_num = int(input())
first_cnt = first_num
second_num = int(input())
second_cnt = second_num
list_numbers = []

for multiply in range(1, second_num + 1):
    list_numbers.append(first_cnt)
    first_cnt += first_num

print(list_numbers)
