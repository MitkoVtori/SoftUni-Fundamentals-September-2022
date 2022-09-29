quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

christmas_spirit = 0
budget = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 10 == 0:
        christmas_spirit -= 20
        budget += tree_skirt + tree_lights + tree_garlands

        if day == days:
            christmas_spirit -= 30

    if day % 5 == 0:
        christmas_spirit += 17
        budget += tree_lights * quantity

    if day % 15 == 0:
        christmas_spirit += 30 # fifth day with garlands

    if day % 3 == 0:
        christmas_spirit += 13
        budget += (tree_garlands + tree_skirt) * quantity

    if day % 2 == 0:
        christmas_spirit += 5
        budget += ornament_set * quantity

print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")
