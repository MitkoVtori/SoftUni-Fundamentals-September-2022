numbers = list(map(int, input().split(', ')))

for group in range(1, 11):
    if len(numbers) == 0:
        break
    group_list = [num for num in numbers if num <= (group * 10)]
    numbers = [num for num in numbers if num not in group_list]
    print(f"Group of {group}0's: {group_list}")