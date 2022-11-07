def string_explosion(string):
    result = ''
    what_left = 0
    for letter in string:
        if len(letter) > 1 and any(map(str.isdigit, letter)):
            what_left += (int(letter[0]) - 1)
            if what_left >= len(letter):
                result += ">"
            else:
                result += ">" + letter[1 + what_left:]
                what_left = 0
        elif len(letter) == 1 and letter.isdigit():
            if int(letter) > 1:
                what_left += (int(letter) - 1)
            result += ">"
        else:
            result += letter

    return result


string = input().split(">")
print(string_explosion(string))