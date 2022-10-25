sequence = input().split(' ')

final_dic = {}
for element in sequence:
    counter = 0
    word = element.lower()
    for curr_element in sequence:
        if curr_element.lower() == word:
            counter += 1
    if counter % 2 != 0:
        final_dic[element.lower()] = element

print(' '.join(final_dic))