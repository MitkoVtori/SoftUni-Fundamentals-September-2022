first_string = input()
second_string = input()
last_string = first_string
for symbol in range(len(second_string)):
    left_string = second_string[:symbol + 1]
    right_string = first_string[symbol + 1:]
    curr_word = left_string + right_string
    if curr_word == last_string:
        continue
    print(curr_word)
    last_string = curr_word
