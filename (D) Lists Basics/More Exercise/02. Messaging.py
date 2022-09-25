list_numbers = input().split(' ')
message = input()
message_list = []

for numbers in list_numbers:
    current_sum = 0
    for integer_numbers in numbers:
        current_sum += int(integer_numbers)

    current_sum %= len(message)

    message_list.append(message[current_sum])
    message = message.replace(message[current_sum], '', 1)

print(''.join(message_list))
