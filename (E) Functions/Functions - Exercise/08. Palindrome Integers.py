def palindrome_integers(numbers):

    for palindrome in range(len(numbers)):
        current_number = numbers[palindrome][::-1]
        if current_number == numbers[palindrome]:
            print("True")
        else:
            print("False")
            
            
list_numbers = input().split(', ')
palindrome_integers(list_numbers)
