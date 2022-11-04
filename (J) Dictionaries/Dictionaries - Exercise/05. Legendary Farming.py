items_dictionary = {}
legendary_item = False
while True:
    items = input().split(' ')

    for index in range(len(items)):
        if index % 2 != 0:
            items[index] = items[index].lower()
            if items[index] not in items_dictionary:
                items_dictionary[items[index]] = int(items[index - 1])
            elif items[index] in items_dictionary:
                items_dictionary[items[index]] += int(items[index - 1])
        for item, value in items_dictionary.items():
            if value >= 250:
                if item == 'shards':
                    print('Shadowmourne obtained!')
                    legendary_item = True
                    items_dictionary['shards'] -= 250
                    break
                elif item == 'fragments':
                    print('Valanyr obtained!')
                    legendary_item = True
                    items_dictionary['fragments'] -= 250
                    break
                elif item == 'motes':
                    print('Dragonwrath obtained!')
                    legendary_item = True
                    items_dictionary['motes'] -= 250
                    break
        if legendary_item:
            break
    if legendary_item:
        break

key_materials = ['motes', 'shards', 'fragments']
# try:
#     print(f'shards: {items_dictionary["shards"]}')
# except KeyError:
#     print('shards: 0')
# try:
#     print(f'fragments: {items_dictionary["fragments"]}')
# except KeyError:
#     print('fragments: 0')
# try:
#     print(f'motes: {items_dictionary["motes"]}')
# except KeyError:
#     print('motes: 0')
if 'shards' in items_dictionary:
    print(f'shards: {items_dictionary["shards"]}')
elif 'shards' not in items_dictionary:
    print('shards: 0')
if 'fragments' in items_dictionary:
    print(f'fragments: {items_dictionary["fragments"]}')
elif 'fragments' not in items_dictionary:
    print('fragments: 0')
if 'motes' in items_dictionary:
    print(f'motes: {items_dictionary["motes"]}')
elif 'motes' not in items_dictionary:
    print('motes: 0')
for curr_item, curr_value in items_dictionary.items():
    if curr_item not in key_materials:
        print(f'{curr_item}: {curr_value}')