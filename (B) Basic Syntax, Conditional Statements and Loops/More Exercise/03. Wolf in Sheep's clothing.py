animal = list(input().split(", "))

if animal[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    if "wolf" in animal:
        animal.reverse()
        for index, value in enumerate(animal):
            if value == "wolf":
                print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
    else:
        pass
