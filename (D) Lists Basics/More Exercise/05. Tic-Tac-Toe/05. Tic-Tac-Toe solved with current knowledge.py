first_row = input().split()
second_row = input().split()
third_row = input().split()

player = 1
name_player = "First"
found = False

while player < 3:
    player = str(player)
    line = [player, player, player]
    if line == first_row or second_row == line or third_row == line: # rows check
        found = True
    for column in range(0, 3):
        if first_row[column] == player and second_row[column] == player and third_row[column] == player: # columns check
            found = True
    if first_row[0] == player and second_row[1] == player and third_row[2] == player: # left diagonal
        found = True
    elif first_row[2] == player and second_row[1] == player and third_row[0] == player: # right diagonal
        found = True
    if found:
        print(f"{name_player} player won")
        break
    player = int(player) + 1
    name_player = "Second"
else:
    print("Draw!")