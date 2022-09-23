key = int(input())
n = int(input())
string = ''

for word in range(n):
    letter = ord(str(input())) + key
    string += chr(letter)

print(string)
