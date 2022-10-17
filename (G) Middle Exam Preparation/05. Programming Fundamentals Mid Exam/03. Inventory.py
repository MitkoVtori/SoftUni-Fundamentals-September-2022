items = input().split(', ')

while True:
    command = input().split(' - ')

    if command[0] == "Craft!":
        break

    current_command = command[0]
    item = command[1]
    old_new_item = command[1].split(':')

    if current_command == "Collect":
        if item not in items:
            items.append(item)

    elif current_command == "Drop":
        if item in items:
            items.remove(item)

    elif current_command == "Combine Items":
        if old_new_item[0] in items:
            index = items.index(old_new_item[0])
            items.insert(index + 1, old_new_item[1])

    elif current_command == "Renew":
        if item in items:
            items.remove(item)
            items.append(item)

print(', '.join(items))



# items = input().split(', ')
#
# while True:
#     command = input().split(' - ')
#
#     if command[0] == "Craft!":
#         break
#
#     if command[0] == "Collect":
#         if command[1] not in items:
#             items.append(command[1])
#
#     elif command[0] == "Drop":
#         if command[1] in items:
#             items.remove(command[1])
#
#     elif command[0] == "Combine Items":
#         old_new_item = command[1].split(':')
#         if old_new_item[0] in items:
#             index = items.index(old_new_item[0])
#             items.insert(index + 1, old_new_item[1])
#
#     elif command[0] == "Renew":
#         if command[1] in items:
#             items.remove(command[1])
#             items.append(command[1])
#
# print(', '.join(items))