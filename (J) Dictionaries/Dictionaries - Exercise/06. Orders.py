products = {}
while True:
    command = input()

    if command == 'buy':
        break

    name, price, quantity = command.split(' ')
    price, quantity = float(price), int(quantity)

    quantity_left = 0
    if name not in products:
        products[name] = {}
        products[name][price] = 0
    else:
        quantity_left = list(products[name].values())
        quantity_left = quantity_left[0]
        products[name].clear()
        products[name] = {}
        products[name][price] = 0

    products[name][price] += quantity + quantity_left

for item in products:
    for key, value in products[item].items():
        result = key * value
        print(f"{item} -> {result:.2f}")