encrypted_message = input()

while True:
    command = input()

    if command == "Decode":
        break

    current_command = command.split("|")

    if current_command[0] == "Move":
        number_of_letters = int(current_command[1])
        for number in range(number_of_letters):
            encrypted_message = encrypted_message[1:] + encrypted_message[0]

    elif current_command[0] == "Insert":
        index = int(current_command[1])
        value = current_command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif current_command[0] == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)


print(f"The decrypted message is: {encrypted_message}")