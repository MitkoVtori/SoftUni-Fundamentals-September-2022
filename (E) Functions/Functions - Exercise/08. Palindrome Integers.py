def palindrome_integer(numbers: list):

    for number in numbers:

        if number == number[::-1]:
            print(True)
            continue
        print(False)


list_numbers = input().split(', ')
palindrome_integer(list_numbers)
