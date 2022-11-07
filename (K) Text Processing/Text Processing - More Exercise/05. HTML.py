title = input()
content = input()
print(f"""
<h1>
{title}
</h1>
<article>
{content}
</article>
""", end='')
comment = input()
while comment != "end of comments":
    print('<div>')
    print(comment)
    print('</div>')
    comment = input()