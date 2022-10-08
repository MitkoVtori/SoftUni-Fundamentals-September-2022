people = int(input())
wagons = list(map(int, input().split(' ')))
no_more_people = False
for spots in range(len(wagons)):
    while wagons[spots] < 4:
        wagons[spots] += 1
        people -= 1
        if people == 0:
            no_more_people = True
            break
    if no_more_people:
        break

if people == 0 and wagons[-1] == 4:
    print(*wagons)
elif people == 0:
    print("The lift has empty spots!")
    print(*wagons)
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*wagons)