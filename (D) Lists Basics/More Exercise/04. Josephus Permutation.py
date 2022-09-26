people = input().split(' ')
kills = int(input())
executed = []
counter = 0
current_index = 0

while len(people) > 0:
    counter += 1

    if counter % kills == 0:
        executed.append(people.pop(current_index))
    else:
        current_index += 1

    if current_index >= len(people):
        current_index = 0

print(str(executed).replace(' ', '').replace('\'', ''))