numbers = input().split()
nums = []

for number in numbers:
    nums.append(int(number))

remover = int(input())

for removing in range(remover):
    nums.remove(min(nums))

print(*nums, sep=', ')
