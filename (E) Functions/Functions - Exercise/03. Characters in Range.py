def characters(char1, char2):

    for chars in range(char1 + 1, char2):
        print(chr(chars), end=' ')


first_char = ord(input())
last_char = ord(input())
characters(first_char, last_char)
