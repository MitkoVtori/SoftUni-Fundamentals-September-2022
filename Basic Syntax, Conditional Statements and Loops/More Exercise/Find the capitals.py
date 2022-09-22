word = input()
list_capitals = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
indices = []
for index, value in enumerate(word):
    if value in list_capitals:
        indices.append(index)
print(indices)
