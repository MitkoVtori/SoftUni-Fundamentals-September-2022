def text_filter(filter_words, string):
    for banned_word in filter_words:
        asterisks = '*' * len(banned_word)
        string = string.replace(banned_word, asterisks)

    return string


banned_words = input().split(', ')
string = input()

print(text_filter(banned_words, string))