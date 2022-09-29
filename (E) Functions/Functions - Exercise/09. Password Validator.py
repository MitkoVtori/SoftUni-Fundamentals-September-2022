password = input()
digits_count = 0
list_letters_and_numbers = []
between_six_and_ten = True
only_letters_and_digits = True
at_least_two_digits = True

if 6 > len(password) or len(password) > 10:
    between_six_and_ten = False
    print('Password must be between 6 and 10 characters')

for lists in range(97, 122 + 1):
    list_letters_and_numbers.append(chr(lists))
    list_letters_and_numbers.append(chr(lists).upper())

for lists_numbers in range(- 1, 10):
    list_letters_and_numbers.append(str(lists_numbers + 1))

for allowed_characters in range(len(password)):
    if password[allowed_characters] not in list_letters_and_numbers:
        only_letters_and_digits = False
        print("Password must consist only of letters and digits")
        break

for index in range(len(password)):
    for numbers in range(- 1, 10):
        number = chr(numbers + 1)
        if str(ord(number)) in password[index]:
            digits_count += 1

if digits_count < 2:
    at_least_two_digits = False
    print("Password must have at least 2 digits")

if between_six_and_ten and only_letters_and_digits and at_least_two_digits:
    print("Password is valid")