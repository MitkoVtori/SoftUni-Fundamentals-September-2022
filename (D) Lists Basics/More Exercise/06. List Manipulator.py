numbers = [int(integer) for integer in input().split()]
command = input().split()

while command[0] != "end":
    even_numbers = [even for even in numbers if even % 2 == 0]
    odd_numbers = [odd for odd in numbers if odd % 2 != 0]

    if command[0] == "exchange":
        if 0 <= int(command[1]) < len(numbers):
            numbers = numbers[int(command[1]) + 1:] + numbers[:int(command[1]) + 1]
        else:
            print(f'Invalid index')

    elif command[0] == "max":
        if command[1] == "even" and even_numbers:
            print((len(numbers) - numbers[::-1].index(max(even_numbers)) - 1))
        elif command[1] == "odd" and odd_numbers:
            print((len(numbers) - numbers[::-1].index(max(odd_numbers)) - 1))
        else:
            print('No matches')

    elif command[0] == "min":
        if command[1] == "even" and even_numbers:
            print((len(numbers) - numbers[::-1].index(min(even_numbers)) - 1))
        elif command[1] == "odd" and odd_numbers:
            print((len(numbers) - numbers[::-1].index(min(odd_numbers)) - 1))
        else:
            print('No matches')

    elif command[0] == "first":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even_numbers[0:int(command[1])])
            else:
                print(odd_numbers[0:int(command[1])])
        else:
            print(f"Invalid count")

    elif command[0] == "last":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even_numbers[-int(command[1]):])
            else:
                print(odd_numbers[-int(command[1]):])
        else:
            print(f"Invalid count")
    command = input().split()

print(numbers)