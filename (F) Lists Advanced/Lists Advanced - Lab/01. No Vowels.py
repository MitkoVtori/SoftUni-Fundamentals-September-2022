word = input()
list_vowels = ["a", "o", "u", "e", "i"]
filtered = [index for index in word if index.lower() not in list_vowels]
print(''.join(filtered))