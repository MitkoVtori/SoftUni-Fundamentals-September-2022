groceries_list = input().split('!')

command = input()
while command != "Go Shopping!":
    indices = command.split(' ')
    current_command = indices[0]
    first_index = indices[1]
    second_index = ''
    if len(indices) == 3:
        second_index = indices[2]

    if current_command == 'Urgent':
        if first_index not in groceries_list:
            groceries_list.insert(0, first_index)

    if current_command == "Unnecessary":
        if first_index in groceries_list:
            groceries_list.remove(first_index)

    if current_command == 'Correct':
        for index, item in enumerate(groceries_list):
            if first_index == item:
                groceries_list[index] = second_index
                break

    if current_command == "Rearrange":
        if first_index in groceries_list:
            groceries_list.remove(first_index)
            groceries_list.append(first_index)

    command = input()

print(*groceries_list, sep=', ')