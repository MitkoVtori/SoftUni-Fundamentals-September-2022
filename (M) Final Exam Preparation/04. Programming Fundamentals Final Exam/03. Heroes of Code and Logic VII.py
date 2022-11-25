heroes = int(input())

heroes_of_code = {}

for current_hero in range(heroes):
    hero, hit_points, mana_points = input().split(' ')
    hit_points, mana_points = int(hit_points), int(mana_points)

    if hit_points > 100:
        hit_points = 100

    if mana_points > 200:
        mana_points = 200

    heroes_of_code[hero] = {hit_points: mana_points}

command = input()
while command != "End":

    try:
        action, hero_name, mp_needed_or_damage_or_amount, spell_name_or_attacker = command.split(" - ")
    except ValueError:
        action, hero_name, mp_needed_or_damage_or_amount = command.split(" - ")

    mp_needed_or_damage_or_amount = int(mp_needed_or_damage_or_amount)

    hp_mp = heroes_of_code[hero_name]
    for key, value in hp_mp.items():
        current_hp = key
        current_mp = value

    if action == "CastSpell":
        mp_needed = mp_needed_or_damage_or_amount
        spell_name = spell_name_or_attacker
        if current_mp >= mp_needed:
            current_mp -= mp_needed
            heroes_of_code[hero_name] = {current_hp: current_mp}
            print(f"{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!")
        elif current_mp < mp_needed:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage = mp_needed_or_damage_or_amount
        attacker = spell_name_or_attacker
        current_hp -= damage
        if current_hp > 0:
            heroes_of_code[hero_name] = {current_hp: current_mp}
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        elif current_hp <= 0:
            del heroes_of_code[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif action == "Recharge":
        amount = mp_needed_or_damage_or_amount
        amount_recovered = amount
        if current_mp + amount > 200:
            amount_recovered = 200 - current_mp
            current_mp = 200
        else:
            current_mp += amount
        heroes_of_code[hero_name] = {current_hp: current_mp}
        print(f"{hero_name} recharged for {amount_recovered} MP!")

    elif action == "Heal":
        amount = mp_needed_or_damage_or_amount
        amount_recovered = amount
        if current_hp + amount > 100:
            amount_recovered = 100 - current_hp
            current_hp = 100
        else:
            current_hp += amount
        heroes_of_code[hero_name] = {current_hp: current_mp}
        print(f"{hero_name} healed for {amount_recovered} HP!")

    command = input()

for name, hp_mp in heroes_of_code.items():

    for hp, mp in hp_mp.items():
        curr_hp = hp
        curr_mp = mp

    print(name)
    print(f"  HP: {curr_hp}")
    print(f"  MP: {curr_mp}")