def digits_letters_characters(string):
    letters = ''
    digits = ''
    characters = ''
    for character in string:
        if character.isalpha():
            letters += character
        elif character.isdigit():
            digits += character
        else:
            characters += character
    return f'{digits}\n{letters}\n{characters}'


string = input()
print(digits_letters_characters(string))