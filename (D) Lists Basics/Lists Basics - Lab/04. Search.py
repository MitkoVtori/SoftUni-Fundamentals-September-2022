number = int(input())
key = input()
list_all = []
filtered_list = []

for word in range(number):
    string = input()
    list_all.append(string)
    if key in string:
        filtered_list.append(string)

print(list_all)
print(filtered_list)
