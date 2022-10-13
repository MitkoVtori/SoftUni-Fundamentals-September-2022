train = int(input())
wagons = [0] * train

while True:
    command = input().split(' ')

    if command[0] == 'End':
        break

    index = int(command[1])
    people = int(command[-1])

    if command[0] == 'add':
        wagons[-1] += index

    if command[0] == 'insert':
        wagons[index] += people

    if command[0] == 'leave':
        wagons[index] -= people

print(wagons)
