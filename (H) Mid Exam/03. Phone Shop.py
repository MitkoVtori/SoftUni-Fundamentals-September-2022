list_phones = input().split(', ')

while True:
    command = input().split(' - ')

    if command[0] == "End":
        break

    phone = command[1]

    if command[0] == "Add":
        if phone not in list_phones:
            list_phones.append(phone)

    if command[0] == "Remove":
        if phone in list_phones:
            list_phones.remove(phone)

    if command[0] == "Bonus phone":
        old_phone, new_phone = phone.split(":")
        if old_phone in list_phones:
            index = list_phones.index(old_phone) + 1
            list_phones.insert(index, new_phone)

    if command[0] == "Last":
        if phone in list_phones:
            index = list_phones.index(phone)
            last_phone = list_phones.pop(index)
            list_phones.append(last_phone)

print(', '.join(list_phones))
