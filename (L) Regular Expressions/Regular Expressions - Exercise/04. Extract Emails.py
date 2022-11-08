import re
string = input()
pattern = re.compile(r"(^|(?<=\s))([A-Za-z0-9])+([\.\-\_][A-Za-z0-9]+)*@([A-Za-z-]+)\.([A-Za-z-]+)([\.A-Za-z-])*(\b|(?=\s))")
emails = re.finditer(pattern, string)
for email in emails:
    print(email[0])