def merge(virus, command):

    first_index = int(command[1])
    second_index = int(command[-1])

    if first_index < 0:
        first_index = 0
    if first_index < second_index:
        length = len(virus)
        if second_index >= length:
            second_index = length - 1
        for num in range(first_index, second_index):
            virus[first_index] += f"{virus.pop(first_index + 1)}"


def divide(virus):

    first_index = int(command[1])
    second_index = int(command[-1])

    length = len(virus[first_index])
    space_between = length // second_index
    string_to_change = virus.pop(first_index)
    result = []
    for end in range(second_index - 1):
        result.append(string_to_change[:space_between])
        string_to_change = string_to_change[space_between:]
    result.append(string_to_change)
    for end in result[::-1]:
        virus.insert(first_index, end)


strings = input().split(' ')
while True:
    command = input().split(' ')

    if command[0] == '3:1':
        break

    if command[0] == "merge":
        merge(strings, command)

    elif command[0] == 'divide':
        divide(strings)

print(' '.join(strings))