elements = input().split(' ')
stock = {}

for index in range(0, len(elements), 2):
    stock[elements[index]] = int(elements[index + 1])

searching_products = input().split(' ')

for curr_product in searching_products:
    if curr_product in stock:
        print(f"We have {stock[curr_product]} of {curr_product} left")
    else:
        print(f"Sorry, we don't have {curr_product}")