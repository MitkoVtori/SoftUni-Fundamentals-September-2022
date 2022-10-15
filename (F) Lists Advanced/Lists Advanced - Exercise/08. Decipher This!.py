sentence = input().split(' ')

number = ''
for index, word in enumerate(sentence):

    letter = ''

    for symbol in word:

        if symbol.isdigit():
            number += symbol
            continue

        letter += symbol

    number = int(number)
    number = chr(number)
    current_word = number + letter
    sentence[index] = current_word

    word = sentence[index]
    word = [char for char in word]
    word[1], word[-1] = word[-1], word[1]
    word = ''.join(word)
    sentence[index] = word

    number = ''

print(*sentence)