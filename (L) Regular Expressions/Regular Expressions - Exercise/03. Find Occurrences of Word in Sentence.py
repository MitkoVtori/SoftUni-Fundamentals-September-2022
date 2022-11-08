import re
string = input().lower()
word = input().lower()
pattern = fr'({word})\b'
matches = re.findall(pattern, string)
print(len(matches))