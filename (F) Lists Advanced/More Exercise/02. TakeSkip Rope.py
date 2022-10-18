string = input()

numbers = []
letters = ''
take_list = []
skip_list = []

final_string = ''

for character in string:
    if character.isdigit():
        numbers.append(int(character))
    else:
        letters += character

for index, num in enumerate(numbers):
    if index % 2 == 0:
        take_list.append(num)
    else:
        skip_list.append(num)

for take, skip in zip(take_list, skip_list):
    if take == 0:
        letters = letters[skip:]
    elif take != 0:
        final_string = final_string + letters[:take]
        letters = letters[skip + take:]

print(final_string)