number_lines = int(input())


def tribonacci(n):
    tribo_list = [1, 0, 0]
    for number in range(n):
        next_num = sum(tribo_list)
        print(next_num, end=' ')
        tribo_list.append(next_num)
        tribo_list.pop(0)


tribonacci(number_lines)