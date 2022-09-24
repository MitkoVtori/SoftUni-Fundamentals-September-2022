n = int(input())
word = input()
words = []
filtered_words = []

for i in range(n):
    string = input()
    if word in string:
        filtered_words.append(string)
    words.append(string)
print(words)
print(filtered_words)
