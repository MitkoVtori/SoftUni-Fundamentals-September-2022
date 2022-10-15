rooms = int(input())

chairs_list = [0] * rooms

total_free_chairs = 0

for current_room in range(rooms):
    chairs = input().split(' ')
    chairs_needed = int(chairs[-1]) - len(chairs[0])
    chairs_list[current_room] += chairs_needed

    if chairs_list[current_room] > 0:
        print(f"{chairs_list[current_room]} more chairs needed in room {current_room + 1}")

    if chairs_list[current_room] < 0:
        total_free_chairs += abs(chairs_list[current_room])
        chairs_list[current_room] = 0

if sum(chairs_list) == 0:
    print(f"Game On, {total_free_chairs} free chairs left")