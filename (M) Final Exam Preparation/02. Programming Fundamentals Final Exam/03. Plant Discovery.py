lines = int(input())

plants_rarity = {}
for plants in range(lines):
    plant, rarity = input().split('<->')
    plants_rarity[plant] = {rarity: []}

command = input()
while command != 'Exhibition':
    exist = True
    current_command, plant = command.split(': ')

    rating_or_new_rarity = 0
    if current_command == 'Rate' or current_command == 'Update':
        plant, rating_or_new_rarity = plant.split(' - ')

    if plant not in plants_rarity:
        exist = False
        print('error')

    if exist:
        value = plants_rarity[plant]
        rarity = ''
        for key in value.keys():
            rarity = key

        if current_command == 'Rate':
            plants_rarity[plant][rarity].append(rating_or_new_rarity)

        elif current_command == 'Update':
            ratings = plants_rarity[plant][rarity]
            plants_rarity[plant] = {rating_or_new_rarity: ratings}

        elif current_command == 'Reset':
            plants_rarity[plant] = {rarity: []}

    command = input()

print('Plants for the exhibition:')
for plant, rarity in plants_rarity.items():
    value = plants_rarity[plant]
    ratings = ''
    for key in value.keys():
        current_rarity = key
        ratings = value[key]
    ratings = [int(num) for num in ratings]
    average_rating = 0
    if ratings:
        average_rating = sum(ratings) / len(ratings)
    print(f'- {plant}; Rarity: {current_rarity}; Rating: {average_rating:.2f}')