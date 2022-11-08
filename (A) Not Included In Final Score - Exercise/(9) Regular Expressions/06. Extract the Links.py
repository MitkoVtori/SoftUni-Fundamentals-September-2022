import re
pattern = r'www\.[a-zA-Z0-9-\.]+\.[a-z]+'
while True:
    string = input()
    if not string:
        break
    valid_domain = re.findall(pattern, string)
    if valid_domain:
        print('\n'.join(valid_domain))