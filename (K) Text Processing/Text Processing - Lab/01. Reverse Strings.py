def reverse_string(string: str):
    reversed_string = string[::-1]
    return f'{string} = {reversed_string}'


string = input()
while string != "end":
    print(reverse_string(string))
    string = input()


# string = input()
# while string != "end":
#     print(string, '=', string[::-1])
#     string = input()