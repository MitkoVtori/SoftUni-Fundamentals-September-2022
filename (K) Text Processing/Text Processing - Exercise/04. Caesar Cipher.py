def caesar_cipher(string):
    result = ''
    for char in string:
         result += chr(ord(char) + 3)
    return result


string = input()
print(caesar_cipher(string))


# print("".join([chr(ord(letter) + 3) for letter in input()]))