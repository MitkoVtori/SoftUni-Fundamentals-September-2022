stops = input()

while True:
    command = input()

    if command == "Travel":
        break

    current_command = command.split(":")

    if current_command[0] == "Add Stop":
        index = int(current_command[1])
        string = current_command[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]

    elif current_command[0] == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            for remove in range(start_index, end_index + 1):
                stops = stops[:start_index] + stops[start_index + 1:]

    if current_command[0] == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)

    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")