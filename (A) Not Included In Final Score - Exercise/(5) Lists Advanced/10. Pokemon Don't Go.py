distances = [int(number) for number in input().split(' ')]

sum_removed_numbers = 0

while len(distances) != 0:

    index = int(input())

    current_num = 0

    if 0 <= index < len(distances):
        current_num = distances.pop(index)

    elif 0 > index:
        current_num = distances[0]
        distances[0] = distances[-1]

    else:
        current_num = distances[-1]
        distances[-1] = distances[0]

    sum_removed_numbers += current_num

    for current_index, current_number in enumerate(distances):
        if current_number <= current_num:
            distances[current_index] += current_num
        else:
            distances[current_index] -= current_num

print(sum_removed_numbers)