def len_password(password):
    if 6 <= len(password) <= 10:
        return True
    return False


def letters_and_digits(password):
    return password.isalnum()


def two_or_more_digits(password, digits):
    for character in password:
        if character.isdigit():
            digits += 1
    if digits > 1:
        return True
    return False


user_password = input()
digits_counter = 0
password_validation_list = [len_password(user_password), letters_and_digits(user_password), two_or_more_digits(user_password, digits_counter)]
if password_validation_list[0] is True and password_validation_list[1] is True and password_validation_list[2] is True:
    print('Password is valid')

if not password_validation_list[0]:
    print("Password must be between 6 and 10 characters")
if not password_validation_list[1]:
    print("Password must consist only of letters and digits")
if not password_validation_list[2]:
    print("Password must have at least 2 digits")
