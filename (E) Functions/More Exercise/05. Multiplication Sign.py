# Write a program that finds if the multiplication of three integers is negative, positive, or zero.
# Try to do this WITHOUT multiplying the 3 numbers!
def multiplication(a, b, c):
    result = None
    if (c > 0 and a < 0 and b < 0) or \
            (b > 0 and a < 0 and c < 0) or \
            (a > 0 and b < 0 and c < 0) or \
            (a > 0 and b > 0 and c > 0):
        result = "positive"

    elif a == 0 or b == 0 or c == 0:
        result = "zero"

    elif a < 0 or b < 0 or c < 0:
        result = "negative"

    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(multiplication(first_number, second_number, third_number))