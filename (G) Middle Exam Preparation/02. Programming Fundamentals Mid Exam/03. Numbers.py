numbers = list(map(int, input().split(' ')))

average = sum(numbers) / len(numbers)
top_five_numbers = []
above_average = []
for numbers_above_average in numbers:
    if numbers_above_average > average:
        above_average.append(numbers_above_average)

if len(above_average) <= 0:
    print("No")
else:
    counter = 0
    for top_five in range(len(above_average)):
        counter += 1
        if counter == 6:
            break
        top_five_numbers.append(max(above_average))
        above_average.remove(max(above_average))
    print(*top_five_numbers)