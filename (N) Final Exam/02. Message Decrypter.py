import re

pattern = r"^(\$|\%)([A-Z][a-z]{2,})\1\:\s(\[(\d+)\])\|(\[(\d+)\])\|(\[(\d+)\])\|$"
lines = int(input())
for msg in range(lines):
    message = input()
    valid_message = re.findall(pattern, message)
    if valid_message:
        tag = valid_message[0][1]
        first_symbol = chr(int(valid_message[0][3]))
        second_symbol = chr(int(valid_message[0][5]))
        third_symbol = chr(int(valid_message[0][7]))
        print(f"{tag}: {first_symbol + second_symbol + third_symbol}")
    elif not valid_message:
        print(f'Valid message not found!')