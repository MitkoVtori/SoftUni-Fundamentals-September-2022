raw_activation_key = input()

command = input()
while command != "Generate":
    operation = command.split(">>>")

    if operation[0] == "Contains":
        substring = operation[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif operation[0] == "Flip":
        upper_lower = operation[1]
        start_index = int(operation[2])
        end_index = int(operation[3])
        if upper_lower == "Upper":
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:]
        elif upper_lower == "Lower":
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]
        print(raw_activation_key)

    elif operation[0] == "Slice":
        start_index = int(operation[1])
        end_index = int(operation[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)

    command = input()

print(f"Your activation key is: {raw_activation_key}")