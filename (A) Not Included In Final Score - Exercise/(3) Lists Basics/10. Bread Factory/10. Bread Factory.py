import sys

entrance = input().split("|")
 
energy = 100
coins = 100
 
for event in entrance:
    split = event.split("-")
 
    if split[0] == "rest":
        energy_from = int(split[1])

        if 100 - energy < energy_from:
            energy_from = 100 - energy

        energy += energy_from
        print(f"You gained {energy_from} energy.")
        print(f"Current energy: {energy}.")
    elif split[0] == "order":
        earn = int(split[1])
 
        if energy >= 30:
            coins += earn
            energy -= 30
            print(f"You earned {earn} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        expense = int(split[1])
        if coins >= expense:
            print(f"You bought {str(split[0])}.")
            coins -= expense
        else:
            print(f"Closed! Cannot afford {str(split[0])}.")
            sys.exit()
 
print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
