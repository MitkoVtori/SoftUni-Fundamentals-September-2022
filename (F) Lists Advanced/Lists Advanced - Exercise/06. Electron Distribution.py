electrons = int(input())

shells = []
index = 0
while electrons > 0:
    index += 1
    max_electrons = 2 * (index * index)

    if max_electrons > electrons:
        shells.append(electrons)
        electrons = 0
        break

    shells.append(max_electrons)
    electrons -= max_electrons

print(shells)