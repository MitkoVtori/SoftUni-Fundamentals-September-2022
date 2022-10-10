energy = int(input())
command = input()
won = 0

while command != 'End of battle':
    distance = int(command)
    if energy >= distance:
        energy -= distance
        won += 1
        if won % 3 == 0:
            energy += won
    else:
        print(f"Not enough energy! Game ends with {won} won battles and {energy} energy")
        break
    command = input()
else:
    print(f"Won battles: {won}. Energy left: {energy}")