def replace_repeating_characters(string):
    for index, char in enumerate(string):
        try:
            if string[index + 1] != char:
                print(char, end='')
        except IndexError:
            print(char, end='')


string = input()
replace_repeating_characters(string)