def substring(remove_string, main_string):
    final_string = main_string
    while remove_string in final_string:
        final_string = final_string.replace(remove_string, '')

    return final_string


first_string = input()
second_string = input()
print(substring(first_string, second_string))