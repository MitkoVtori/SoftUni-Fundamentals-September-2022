lines = int(input())

for numbers in range(lines):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break

else:
    print("All numbers are even.")
