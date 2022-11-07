def ascii_sumator(first_char, second_char, sequence):
    starting_character = ord(first_char)
    ending_character = ord(second_char)
    sum_characters = 0
    for char in sequence:
        number = ord(char)
        if starting_character < number < ending_character:
            sum_characters += number

    return sum_characters


start_char = input()
end_char = input()
string = input()
print(ascii_sumator(start_char, end_char, string))