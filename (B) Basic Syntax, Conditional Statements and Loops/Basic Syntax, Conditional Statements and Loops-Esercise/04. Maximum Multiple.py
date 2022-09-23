divisior = int(input())
boundary = int(input())
curr_num = boundary

for i in range(boundary, divisior, - 1):
    if 0 < curr_num <= boundary and curr_num % divisior == 0:
        print(curr_num)
        break
    curr_num -= 1
