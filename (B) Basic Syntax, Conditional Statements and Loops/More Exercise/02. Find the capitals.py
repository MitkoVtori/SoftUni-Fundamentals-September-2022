word = input()
list_capitals = []
# Making this for loop so I don't have to write all the capital letters
for capitals in range(65, 90 + 1):
    list_capitals.append(chr(capitals))
indices = []
for index, value in enumerate(word):
    if value in list_capitals:
        indices.append(index)
print(indices)
