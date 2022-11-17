pieces = int(input())

pieces_collection = {}
for num in range(pieces):
    piece, composer, key = input().split('|')
    pieces_collection[piece] = {composer: key}

while True:
    command = input()

    if command == "Stop":
        break

    current_command = command.split('|')

    if current_command[0] == 'Add':
        piece = current_command[1]
        composer = current_command[2]
        key = current_command[3]
        if piece in pieces_collection:
            print(f'{piece} is already in the collection!')
            continue
        pieces_collection[piece] = {composer: key}
        print(f'{piece} by {composer} in {key} added to the collection!')

    elif current_command[0] == 'Remove':
        piece = current_command[1]
        if piece in pieces_collection:
            del pieces_collection[piece]
            print(f'Successfully removed {piece}!')
            continue
        print(f'Invalid operation! {piece} does not exist in the collection.')

    elif current_command[0] == 'ChangeKey':
        piece = current_command[1]
        key = current_command[2]
        if piece in pieces_collection:
            value = pieces_collection[piece]
            composer = ''
            for k in value.keys():
                composer = k
            pieces_collection[piece][composer] = key
            print(f'Changed the key of {piece} to {key}!')
            continue
        print(f'Invalid operation! {piece} does not exist in the collection.')


for piece, value in pieces_collection.items():
    curr_value = value.keys()
    for k in curr_value:
        composer = k
        key = pieces_collection[piece][composer]
        print(f'{piece} -> Composer: {composer}, Key: {key}')