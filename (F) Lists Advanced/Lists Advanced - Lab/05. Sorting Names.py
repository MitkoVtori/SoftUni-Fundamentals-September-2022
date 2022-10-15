names = input().split(', ')
sorted_names = sorted(names, key=lambda item: (-len(item), item))
print(sorted_names)
