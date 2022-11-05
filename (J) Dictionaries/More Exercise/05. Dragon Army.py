dragons = int(input())

dragon_information = {}
damage_d, health_d, armor_d = "damage", "health", "armor"


def create_dragon(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor):
    dragon_information[dragon_type] = dragon_information.get(dragon_type, dict())
    dragon_information[dragon_type][dragon_name] = dragon_information.get(dragon_name, dict())
    dragon_information[dragon_type][dragon_name][damage_d] = dragon_damage
    dragon_information[dragon_type][dragon_name][health_d] = dragon_health
    dragon_information[dragon_type][dragon_name][armor_d] = dragon_armor


def show_result():
    for color in dragon_information:
        damage, health, armor = 0, 0, 0
        for name in dragon_information[color]:
            damage += dragon_information[color][name][damage_d]
            health += dragon_information[color][name][health_d]
            armor += dragon_information[color][name][armor_d]
        total_dragons = len(dragon_information[color])
        print(f"{color}::({(damage / total_dragons):.2f}/{(health / total_dragons):.2f}/{(armor / total_dragons):.2f})")
        for name in sorted(dragon_information[color].keys()):
            print(
                f"-{name} -> damage: {dragon_information[color][name][damage_d]}, health: {dragon_information[color][name][health_d]}, armor: {dragon_information[color][name][armor_d]}")


for index in range(dragons):
    dragon_type, dragon_name, damage, health, armor = input().split()
    if damage == "null":
        dragon_damage = 45
    else:
        dragon_damage = int(damage)
    if health == "null":
        dragon_health = 250
    else:
        dragon_health = int(health)
    if armor == "null":
        dragon_armor = 10
    else:
        dragon_armor = int(armor)
    create_dragon(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor)

show_result()