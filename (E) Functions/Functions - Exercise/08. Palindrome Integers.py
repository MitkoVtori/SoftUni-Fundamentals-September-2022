numbers = input().split(', ')

for palindrome in range(len(numbers)):
    current_number = numbers[palindrome][::-1]
    if current_number == numbers[palindrome]:
        print("True")
    else:
        print("False")