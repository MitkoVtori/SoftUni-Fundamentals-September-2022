n = int(input())
word = input()
words = []
filtered_words = []

for i in range(n):
    string = input()
    if word not in string:
        words.append(string)
    else:
        words.append(string)
        filtered_words.append(string)
print(words)
print(filtered_words)