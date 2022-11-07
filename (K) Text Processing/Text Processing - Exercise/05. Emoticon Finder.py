def emoticon_finder(string):
    for index, char in enumerate(string):
        if char == ':':
            print(f'{char}{string[index + 1]}')


string = input()
emoticon_finder(string)