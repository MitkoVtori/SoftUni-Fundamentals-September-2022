message = input()

command = input()
while command != "Reveal":
    error = False

    current_command = command.split(':|:')
    instruction = current_command[0]
    index = current_command[1]
    substring = current_command[1]

    try:
        replacement = current_command[2]
    except IndexError:
        '''replacement doesn't exist'''

    if instruction == "InsertSpace":
        index = int(index)
        message = message[:index] + ' ' + message[index:]

    elif instruction == "Reverse":
        if substring in message:
            index = message.index(substring)
            how_long = len(substring)
            for msg in range(how_long):
                message = message[:index] + message[index+1:]
            message += substring[::-1]
        else:
            error = True
            print("error")

    elif instruction == "ChangeAll":
        message = message.replace(substring, replacement)

    if not error:
        print(message)

    command = input()

print(f"You have a new text message: {message}")