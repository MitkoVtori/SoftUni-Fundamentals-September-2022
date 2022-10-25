bakery = input().split(' ')
bakery_stock = {}

for index in range(0, len(bakery), 2):
    bakery_stock[bakery[index]] = int(bakery[index + 1])

print(bakery_stock)