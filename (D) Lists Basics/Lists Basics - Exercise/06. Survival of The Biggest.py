numbers = input().split()
nums = []

for n in numbers:
    nums.append(int(n))

remover = int(input())

for _ in range(remover):
    nums.remove(min(nums))

print(*nums, sep=', ')
