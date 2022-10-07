def perfect_num(num, divisor):
    for divide in range(1, num):
        if num % divide == 0:
            divisor += divide

    if divisor == num:
        return "We have a perfect number!"
    return "It's not so perfect."

    
number = int(input())
divisors = 0
print(perfect_num(number, divisors))
