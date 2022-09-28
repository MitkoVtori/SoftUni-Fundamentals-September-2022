def type_of_grade(grade):
    if 2.00 <= score <= 2.99:
        result = 'Fail'
    elif 3.00 <= score <= 3.49:
        result = "Poor"
    elif 3.50 <= score <= 4.49:
        result = "Good"
    elif 4.50 <= score <= 5.49:
        result = "Very Good"
    elif 5.50 <= score <= 6.00:
        result = "Excellent"
    else:
        result = "Incorrect"

    return result


score = float(input())
print(type_of_grade(score))
