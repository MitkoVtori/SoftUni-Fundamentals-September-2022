liked_meals = {}
disliked_meals_count = 0
command = input()
while command != "Stop":
    like_dislike, guest, meal = command.split('-')

    if like_dislike == "Like":
        if guest in liked_meals and meal not in liked_meals[guest]:
            liked_meals[guest].append(meal)
        elif guest not in liked_meals:
            liked_meals[guest] = [meal]

    elif like_dislike == "Dislike":
        if guest not in liked_meals:
            print(f"{guest} is not at the party.")
        elif meal not in liked_meals[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            disliked_meals_count += 1
            liked_meals[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")

    command = input()

for guest, meals in liked_meals.items():
    print(f"{guest}: {', '.join(meals)}")

print("Unliked meals:", disliked_meals_count)