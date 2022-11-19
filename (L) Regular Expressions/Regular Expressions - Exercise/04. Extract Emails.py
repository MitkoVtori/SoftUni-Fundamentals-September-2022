import re
 
string = input()
pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b'
emails = re.findall(pattern, string)
for email in emails:
    print(email[0])
