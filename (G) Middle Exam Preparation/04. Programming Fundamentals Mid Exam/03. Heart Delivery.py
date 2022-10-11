neighborhood = list(map(int, input().split('@')))
last_house = 0
jumps_count = 0
while True:
    command = input()

    if command == 'Love!':
        break
    jump_command = command.split(' ')
    index = int(jump_command[1])
    jumps_count += 1

    if jumps_count > 1:
        index += last_house
    if index >= len(neighborhood):
        jumps_count = 0
        index = 0

    last_house = index

    if neighborhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")
        continue

    neighborhood[index] -= 2
    if neighborhood[index] == 0:
        print(f"Place {index} has Valentine's day.")

    continue

print(f"Cupid's last position was {last_house}.")

failed_house = 0
for valentine in neighborhood:
    if valentine > 0:
        failed_house += 1

if not failed_house:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_house} places.")