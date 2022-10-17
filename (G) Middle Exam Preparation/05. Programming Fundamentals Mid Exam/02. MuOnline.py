command_rooms = input().split('|')

health = 100
bitcoins = 0
best_room = 0
dead = False

for index, value in enumerate(command_rooms):
    best_room += 1
    current_room = value.split(' ')
    number = int(current_room[1])
    index += 1
    if current_room[0] == "potion":
        if health + number > 100:
            number = 100 - health
            health = 100
        else:
            health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif current_room[0] == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        if number >= health:
            dead = True
            print(f"You died! Killed by {current_room[0]}.")
            print(f"Best room: {best_room}")
            break
        else:
            health -= number
            print(f'You slayed {current_room[0]}.')

if not dead:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f"Health: {health}")