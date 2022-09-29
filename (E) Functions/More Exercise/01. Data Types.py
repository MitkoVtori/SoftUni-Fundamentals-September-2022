type_command = input()
command = input()

if type_command == 'int':
    print(int(command) * 2)
elif type_command == "real":
    print(f"{float(command) * 1.5:.2f}")
else:
    print(f"${command}$")