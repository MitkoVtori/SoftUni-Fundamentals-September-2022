num = int(input())

for start_stars in range(1, num + 1):
    print(start_stars * '*')

for end_stars in range(num - 1, 0, - 1):
    print(end_stars * '*')
