import re

emoji_pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"
digits_pattern = r"\d"

string = input()

threshold = re.findall(digits_pattern, string)

cool_threshold = 1

for index in range(len(threshold)):
    cool_threshold *= int(threshold[index])

print(f"Cool threshold: {cool_threshold}")

emojis = re.findall(emoji_pattern, string)
print(len(emojis), "emojis found in the text. The cool ones are:")

for emoji in emojis:
    ascii_values = [ord(char) for char in emoji[1]]
    sum_values = sum(ascii_values)
    if sum_values >= cool_threshold:
        print(emoji[0] + emoji[1] + emoji[0])