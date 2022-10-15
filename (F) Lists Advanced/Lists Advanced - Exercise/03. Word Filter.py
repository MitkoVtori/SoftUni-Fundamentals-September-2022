words = input().split(' ')
words_list = [word for word in words if len(word) % 2 == 0]
print('\n'.join(words_list))


# print('\n'.join([word for word in input().split(' ') if len(word) % 2 == 0]))