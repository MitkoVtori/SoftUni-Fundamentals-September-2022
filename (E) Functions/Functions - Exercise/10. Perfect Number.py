number = int(input())
divisors = 0

for divide in range(1, number):
    if number % divide == 0:
        divisors += divide

if divisors == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")