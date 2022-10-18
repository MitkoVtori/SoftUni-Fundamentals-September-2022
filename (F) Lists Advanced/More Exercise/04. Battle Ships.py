rows = int(input())
ships_list = []

for current_row in range(rows):
    ships = input().split(' ')
    ships_list.append(ships)
attacked_squares = input().split(' ')

destroyed_counter = 0
for attack in attacked_squares:
    current_attack = attack.split('-')
    row = int(current_attack[0])
    col = int(current_attack[1])

    current_ship = ships_list[row]
    curr_ship = int(current_ship[col])

    if curr_ship > 0:
        curr_ship -= 1
        if curr_ship == 0:
            destroyed_counter += 1

    current_ship[col] = str(curr_ship)
    ships_list[row] = current_ship

print(destroyed_counter)