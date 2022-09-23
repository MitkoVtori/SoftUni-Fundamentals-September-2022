items = input().split("|")
budget = float(input())
bought = list()
profit = 0

for item in items:
    indx = item.split('->')
    clothes = indx[0]
    price = float(indx[1])

    accepted = False

    if price > budget:
        continue

    if clothes == 'Clothes':
        if price <= 50.00:
            budget -= price
            accepted = True
    elif clothes == 'Shoes':
        if price <= 35.00:
            budget -= price
            accepted = True
    elif clothes == 'Accessories':
        if price <= 20.50:
            budget -= price
            accepted = True
    if accepted:
        res = float("{:.2f}".format(price * 1.40))
        bought.append(price * 1.40)
        profit += (price * 1.40) - price

for elem in bought:
    budget += elem


def l_to_s(s):
    string_one = ''
    for element in s:
        string_one += "{:.2f}".format(element) + " "
    return string_one


print(l_to_s(bought))
print(f'Profit: {profit:.2f}')

if budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
