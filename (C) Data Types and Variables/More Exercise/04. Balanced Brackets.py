n = int(input())
balanced = 0
last_bracket = ''
for i in range(n):
    string = input()
    if string == "(":
        balanced += 1
        last_bracket = "("
        if balanced > 1:
            print("UNBALANCED")
            exit()
    elif string == ")":
        balanced -= 1
        last_bracket = ")"
if balanced == 0 and last_bracket != "(":
    print("BALANCED")
else:
    print("UNBALANCED")