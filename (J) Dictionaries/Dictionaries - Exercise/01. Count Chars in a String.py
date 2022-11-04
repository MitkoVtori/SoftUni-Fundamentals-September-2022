words = input().split(" ")
characters_dictionary = {}
for index in range(len(words)):
    for char in words[index]:
        if char in characters_dictionary:
            characters_dictionary[char] += 1
        elif char not in characters_dictionary:
            characters_dictionary[char] = 1

for character, value in characters_dictionary.items():
    print(f"{character} -> {value}")