miner_dictionary = {}
while True:
    resource = input()

    if resource == "stop":
        break

    quantity = int(input())

    if resource in miner_dictionary:
        miner_dictionary[resource] += quantity

    elif resource not in miner_dictionary:
        miner_dictionary[resource] = quantity


for item, quantity in miner_dictionary.items():
    print(f'{item} -> {quantity}')