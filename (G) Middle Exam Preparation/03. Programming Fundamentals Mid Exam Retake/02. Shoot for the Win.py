targets = list(map(int, input().split(' ')))
targets_counter = 0
while True:
    command = input()

    if command == 'End':
        break

    current_target = int(command)
    if current_target >= len(targets):
        continue
    if targets[current_target] == -1:
        continue

    for index in range(len(targets)):
        if targets[index] == -1:
            continue
        if index == current_target:
            continue
        elif targets[index] > targets[current_target]:
            targets[index] -= targets[current_target]
        else:
            targets[index] += targets[current_target]

    targets[current_target] = -1
    targets_counter += 1

print(f"Shot targets: {targets_counter} ->", *targets, sep=' ')
