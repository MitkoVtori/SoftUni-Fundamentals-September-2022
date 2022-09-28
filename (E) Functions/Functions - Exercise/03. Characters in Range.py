def characters(a, b):

    for chars in range(a + 1, b):
        print(chr(chars), end=' ')


first_char = ord(input())
last_char = ord(input())
characters(first_char, last_char)