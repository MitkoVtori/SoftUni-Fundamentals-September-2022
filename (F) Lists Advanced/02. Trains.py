number_wagons = int(input())
train = [0 for wagons in range(number_wagons)]

command = input()
while command != "End":

    data = command.split(' ')

    if 'add' in data:
        train[-1] += int(data[-1])

    elif 'insert' in data:
        train[int(data[1])] += int(data[-1])

    else:
        train[int(data[1])] -= int(data[-1])

    command = input()

print(train)