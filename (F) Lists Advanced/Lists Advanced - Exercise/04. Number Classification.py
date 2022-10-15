def positive(numbers):
    positive_numbers = [str(num) for num in numbers if num >= 0]
    return f"Positive: {', '.join(positive_numbers)}"


def negative(numbers):
    negative_numbers = [str(num) for num in numbers if num < 0]
    return f"Negative: {', '.join(negative_numbers)}"


def even(numbers):
    even_numbers = [str(num) for num in numbers if num % 2 == 0]
    return f"Even: {', '.join(even_numbers)}"


def odd(numbers):
    odd_numbers = [str(num) for num in numbers if num % 2 != 0]
    return f"Odd: {', '.join(odd_numbers)}"


list_numbers = list(map(int, input().split(', ')))
print(positive(list_numbers))
print(negative(list_numbers))
print(even(list_numbers))
print(odd(list_numbers))

