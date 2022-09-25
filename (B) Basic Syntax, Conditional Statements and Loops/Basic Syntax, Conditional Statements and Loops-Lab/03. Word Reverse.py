word = input()

reverse_word = ''

for reverse in range(len(word) - 1, -1, -1):
    reverse_word += word[reverse]
print(reverse_word)
