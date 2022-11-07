def characters_multiply(first_string, second_string):
    first_string = [ord(num) for num in first_string]
    second_string = [ord(num) for num in second_string]
    first_string_len = len(first_string)
    second_string_len = len(second_string)
    if first_string_len > second_string_len:
        for index in range(first_string_len - second_string_len):
            second_string.append(1)
    elif first_string_len < second_string_len:
        for index in range(second_string_len - first_string_len):
            first_string.append(1)
    print(sum([first_string[index] * second_string[index] for index in range(len(first_string))]))


string_one, string_two = input().split()
characters_multiply(string_one, string_two)