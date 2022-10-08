total_price = 0
price_without_taxes = 0
taxes = 0
while True:
    price = input()

    if price == 'special' or price == 'regular':
        break
   
    price = float(price)
          
    if price < 0:
        print('Invalid price!')
        continue
    total_price += price
    price_without_taxes += price
    taxes += price * 0.20

total_price += taxes
if price == 'special':
    total_price *= 0.90
if total_price == 0:
    print('Invalid order!')
if total_price > 0:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
