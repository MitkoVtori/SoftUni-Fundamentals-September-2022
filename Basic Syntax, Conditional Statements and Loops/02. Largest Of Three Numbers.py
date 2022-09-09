import sys

max_num = -sys.maxsize

for i in range(3):
    num = float(input())

    if num >= max_num:
        max_num = num
print(f"{max_num:.0f}")
