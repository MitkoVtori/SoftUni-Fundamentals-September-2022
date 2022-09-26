list_numbers = input().split(', ')
zero_cnt = 0
final_list = []

for numbers in list_numbers:
    if numbers != '0':
        final_list.append(int(numbers))
        continue
    zero_cnt += 1

for zeros in range(zero_cnt):
    final_list.append(0)
print(final_list)
