def valid_username(username):
    allowed_symbols = ['_', '-']
    if 3 <= len(username) <= 16:
        for character in username:
            if character.isalnum() or character in allowed_symbols:
                continue
            return
    else:
        return
    print(username)


list_usernames = input().split(', ')
while len(list_usernames):
    name = list_usernames[0]
    valid_username(name)
    list_usernames.pop(0)