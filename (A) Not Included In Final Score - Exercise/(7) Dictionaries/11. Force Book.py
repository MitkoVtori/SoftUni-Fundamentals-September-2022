force_dictionary = {}


def add_user(name, side):
    for users in force_dictionary.values():
        if name in users:
            return
    force_dictionary[side] = force_dictionary.get(side, []) + [name]


def switch_side(side, name):
    for sides, users in force_dictionary.items():
        if name in users:
            force_dictionary[sides].remove(name)
            break
    force_dictionary[side] = force_dictionary.get(side, []) + [name]
    print(f"{name} joins the {side} side!")


command = input()

while command != "Lumpawaroo":
    if "|" in command:
        side, name = command.split(" | ")
        add_user(name, side)
    elif "->" in command:
        side, name = command.split(" -> ")
        switch_side(name, side)

    command = input()

for side, members in force_dictionary.items():
    if members:
        print(f"Side: {side}, Members: {len(members)}")
        for user in members:
            print(f"! {user}")