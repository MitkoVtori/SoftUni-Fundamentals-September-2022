n = int(input())
command_even = "even"
command_odd = "odd"
command_positive = "positive"
command_negative = "negative"
my_list = []
filtered_numbers = []

for num in range(n):
    curr_num = int(input())
    my_list.append(curr_num)

command = input()

for number in my_list:
    filtered_command = (
        (command == command_even and number % 2 == 0) or
        (command == command_odd and number % 2 != 0) or
        (command == command_positive and number >= 0) or
        (command == command_negative and number < 0)
    )

    if filtered_command:
        filtered_numbers.append(number)

print(filtered_numbers)
