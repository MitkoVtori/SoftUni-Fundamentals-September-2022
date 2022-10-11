food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
enough = True
pig_weight = float(input()) * 1000
days = 0
while True:
    days += 1
    food -= 300
    if days % 2 == 0:
        hay -= food * 0.05
    if days % 3 == 0:
        cover -= pig_weight / 3
    if food <= 0 or hay <= 0 or cover <= 0:
        enough = False
        break

    if days == 30:
        break

if food <= 0 or hay <= 0 or cover <= 0:
    if food <= 0 or hay <= 0 or cover <= 0 and days < 30 or not enough:
        print("Merry must go to the pet store!")
    else:
        pass
else:
    food /= 1000
    hay /= 1000
    cover /= 1000
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")