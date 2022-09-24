import sys

max_number = -sys.maxsize

for largest in range(3):
    number = float(input())

    if number > max_number:
        max_number = number
print(f"{max_number:.0f}")
