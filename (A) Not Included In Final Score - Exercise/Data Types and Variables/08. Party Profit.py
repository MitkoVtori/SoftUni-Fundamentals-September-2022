companions = int(input())
days_adventure = int(input())
coins = 0

for day in range(1, days_adventure + 1):
        # Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave.
    if day % 10 == 0:
        companions -= 2
        # Every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day
    if day % 15 == 0:
        companions += 5

    # Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
    coins += (50 - (2 * companions))

# Every 3rd (third) day, you organize a motivational party, spending 3 coins per companion for drinking water.
    if day % 3 == 0:
        coins -= (3 * companions)
# Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion.
# But if you have a motivational party the same day, you spend additional 2 coins per companion.
    if day % 5 == 0:

        coins += (20 * companions)

        if day % 3 == 0:
            coins -= (2 * companions)

coins_per_companion = int(coins / companions)
print(f"{companions} companions received {coins_per_companion} coins each.")
