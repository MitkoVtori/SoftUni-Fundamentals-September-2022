def repeat_string(strings):
    for word in strings:
        length_word = len(word)
        print(word * length_word, end='')


strings = input().split(' ')
repeat_string(strings)