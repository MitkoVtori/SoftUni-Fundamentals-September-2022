products = {}
total_products = 0
total_quantity = 0
command = input()
while command != "statistics":
    product = command.split(": ")
    if product[0] in products:
        products[product[0]] += int(product[1])
    else:
        products[product[0]] = int(product[1])
        total_products += 1

    total_quantity += int(product[1])

    command = input()

print(f"Products in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")