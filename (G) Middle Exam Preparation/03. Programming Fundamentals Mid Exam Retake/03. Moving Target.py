targets = list(map(int, input().split(' ')))

while True:
    command = input()
    if command == 'End':
        break
    indexes = command.split(' ')
    index = int(indexes[1])
    power = int(indexes[2])
    value = int(indexes[2])
    radius = int(indexes[2])
    if indexes[0] == "Shoot":
        if index >= len(targets) or index < 0:
            continue
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    elif indexes[0] == "Add":
        if index >= len(targets) or index < 0:
            print("Invalid placement!")
            continue
        else:
            targets.insert(index, value)
    else:
        if index >= len(targets) or index + radius >= len(targets) or index - radius < 0:
            print("Strike missed!")
            continue
        for indices in range(radius):
            targets.pop(index - 1)
            targets.pop(index)
        targets.pop(index - radius)

print(*targets, sep="|")
