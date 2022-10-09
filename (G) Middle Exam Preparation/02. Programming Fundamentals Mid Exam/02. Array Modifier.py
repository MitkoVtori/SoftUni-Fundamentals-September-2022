array = list(map(int, input().split(' ')))

while True:
    command = input()
    if command == 'end':
        break

    if command == 'decrease':
        for element in range(len(array)):
            array[element] -= 1
        continue
    indexes = command.split(' ')
    index1 = int(indexes[1])
    index2 = int(indexes[2])
    if indexes[0] == 'swap':
        array[index1], array[index2] = array[index2], array[index1]
    if indexes[0] == 'multiply':
        array[index1] *= array[index2]

print(*array, sep=', ')