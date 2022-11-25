password = input()

command = input()
while command != "Done":
    activity = command.split(' ')

    if activity[0] == "TakeOdd":
        string = [char for index, char in enumerate(password) if index % 2 != 0]
        password = ''.join(string)
        print(password)

    elif activity[0] == "Cut":
        index = int(activity[1])
        length = int(activity[2])
        password = password[:index] + password[index + length:]
        print(password)

    elif activity[0] == "Substitute":
        substring = activity[1]
        substitute = activity[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")