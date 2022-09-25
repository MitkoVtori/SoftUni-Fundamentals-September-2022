list_numbers = input().split()
big_numbers = []

for number in list_numbers:
    big_numbers.append(int(number))

remover = int(input())

for removing in range(remover):
    big_numbers.remove(min(big_numbers))

print(*nums, sep=', ')
