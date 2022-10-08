from math import floor

elements = input().split(' ')
number_of_moves = 0
while True:
    command = input()
    if command == "end":
        break
    if len(elements) < 2:
        continue
    number_of_moves += 1
    indexes = command.split(' ')
    first_index = indexes[0]
    second_index = indexes[1]
    first_index = int(first_index)
    second_index = int(second_index)
    if first_index == second_index or first_index < 0 or second_index < 0 or first_index > len(elements) - 1 \
       or second_index > len(elements) - 1:
        middle_elements = len(elements) / 2
        middle_elements = floor(middle_elements)
        elements.insert(middle_elements, f"-{number_of_moves}a")
        elements.insert(middle_elements, f"-{number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue
    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        if second_index > 0:
            second_index -= 1
        elements.pop(first_index)
        elements.pop(second_index)
        continue
    else:
        print("Try again!")
        continue

if len(elements) < 2:
    print(f"You have won in {number_of_moves} turns!")
else:
    print("Sorry you lose :(")
    print(*elements)