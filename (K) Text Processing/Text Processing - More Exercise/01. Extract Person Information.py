def extract_information(string):
    name = ''
    age = ''
    for index, char in enumerate(string):
        if char == '@':
            while True:
                index += 1

                if string[index] == '|':
                    break

                name += string[index]
        elif char == '#':
            while True:
                index += 1

                if string[index] == '*':
                    break

                age += string[index]

    return f'{name} is {age} years old.'


string_lines = int(input())

for person_information in range(string_lines):
    information = input()
    print(extract_information(information))