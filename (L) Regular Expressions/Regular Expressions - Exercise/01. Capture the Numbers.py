import re
pattern = r'\d+'
digits = []
while True:
    string = input()
    if string:
        numbers = re.findall(pattern, string)
        if numbers:
            digits.append(' '.join(numbers))
        continue
    break

print(' '.join(digits))