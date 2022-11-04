phonebook = {}
while True:
    command = input()

    if command.isdigit():
        break

    name, number = command.split('-')

    phonebook[name] = number

for contact in range(int(command)):
    contact_name = input()
    if contact_name not in phonebook:
        print(f'Contact {contact_name} does not exist.')
    elif contact_name in phonebook:
        print(f'{contact_name} -> {phonebook[contact_name]}')