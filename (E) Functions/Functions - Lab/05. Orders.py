def total_price(bought, quantity):
    if bought == "coffee":
        result = 1.50 * quantity
    elif bought == "water":
        result = 1.00 * quantity
    elif bought == "coke":
        result = 1.40 * quantity
    elif bought == "snacks":
        result = 2.00 * quantity
    else:
        result = None

    print(f"{result:.2f}")

    
bought = input()
quantity = float(input())
total_price(bought, quantity)
