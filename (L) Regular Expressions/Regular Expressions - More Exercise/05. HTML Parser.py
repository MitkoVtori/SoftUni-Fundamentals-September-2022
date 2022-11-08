import re

text = input()

pattern_title = r"(?:<title>)(?P<title>.+)(?:</title>)"
pattern_body = r"(?:<body>)(?P<body>.+)(?:</body>)"
title = re.search(pattern_title, text).group("title")
body = re.search(pattern_body, text).group("body")
title = re.sub(r"[ ]+", " ", re.sub(r"\\n|\\t", "", re.sub(r"<[^>]*>", "", title)))
body = re.sub(r"[ ]+", " ", re.sub(r"\\n|\\t", "", re.sub(r"<[^>]*>", "", body)))
print(f"Title: {title}")
print(f"Content: {body}")