import re

name_of_participants = {name.replace(" ", ""): 0 for name in input().split(",")}
racer_code = input()
letters_d = re.compile(r"([A-Za-z])")
numbers_d = re.compile(r"([0-9])")
while racer_code != "end of race":
    find_name = "".join(re.findall(letters_d, racer_code))
    find_numbers = sum(int(num) for num in re.findall(numbers_d, racer_code))
    if find_name in name_of_participants.keys():
        name_of_participants[find_name] += find_numbers
    racer_code = input()

name_of_participants = sorted(name_of_participants.items(), key=lambda x: -x[1])

print(f"1st place: {name_of_participants[0][0]}")
print(f"2nd place: {name_of_participants[1][0]}")
print(f"3rd place: {name_of_participants[2][0]}")