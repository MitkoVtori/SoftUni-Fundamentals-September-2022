string = input()

command = input()
while command != "Finish":
    decrypting_command = command.split(" ")

    if decrypting_command[0] == "Replace":
        current_char = decrypting_command[1]
        new_char = decrypting_command[2]
        string = string.replace(current_char, new_char)
        print(string)

    elif decrypting_command[0] == "Cut":
        start_index = int(decrypting_command[1])
        end_index = int(decrypting_command[2])
        if 0 <= start_index < len(string) and 0 <= end_index < len(string):
            string = string[:start_index] + string[end_index+1:]
            print(string)
        else:
            print("Invalid indices!")

    elif decrypting_command[0] == "Make":
        if decrypting_command[1] == "Upper":
            string = string.upper()
        else:
            string = string.lower()
        print(string)

    elif decrypting_command[0] == "Check":
        substring = decrypting_command[1]
        if substring in string:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")

    elif decrypting_command[0] == "Sum":
        start_index = int(decrypting_command[1])
        end_index = int(decrypting_command[2])
        if 0 <= start_index < len(string) and 0 <= end_index < len(string):
            substring = string[start_index:end_index+1]
            ascii_sum = 0
            for ascii in substring:
                ascii_sum += ord(ascii)
            print(ascii_sum)
        else:
            print("Invalid indices!")

    command = input()