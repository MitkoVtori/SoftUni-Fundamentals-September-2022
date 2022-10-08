def characters(first, second):

    for chars in range(ord(first) + 1, ord(second)):
        print(chr(chars), end=' ')


first_character = input()
second_character = input()
characters(first_character, second_character)
