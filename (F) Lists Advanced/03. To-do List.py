todo_list = []
ten_list = []

while True:
    todo = input()

    if todo == "End":
        break

    if todo.split('-')[0] == '10':
        todo = todo.split('-')
        ten_list.append(todo[1])
        continue

    todo_list.append(todo)

todo_list = sorted(todo_list)
todo_final_list = []

for index in range(len(todo_list)):
    to_do = todo_list[index].split('-')
    todo_final_list.append(to_do[1])

for tens in range(len(ten_list)):
    todo_final_list.append(ten_list[tens])

print(todo_final_list)