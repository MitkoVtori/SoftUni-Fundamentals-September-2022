# We have a fighter, here we see how much lost fights he has.
lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
# Here we count how many times he broke his shield.
shield_broken = 0
# These are our equipment costs.
expenses = 0

for lost in range(1, lost_fights_count + 1):
    # Every second lost game, his helmet is broken.
    if lost % 2 == 0:
        expenses += helmet_price

    # Every third lost game, his sword is broken.
    if lost % 3 == 0:
        expenses += sword_price

    # When both his sword and helmet are broken in the same lost fight, his shield also breaks.
    if lost % 2 == 0 and lost % 3 == 0:
        shield_broken += 1
        expenses += shield_price

        # Every second time his shield brakes, his armor also needs to be repaired.
        if shield_broken % 2 == 0:
            expenses += armor_price

# Finally, we print the expenses.
print(f"Gladiator expenses: {expenses:.2f} aureus")
