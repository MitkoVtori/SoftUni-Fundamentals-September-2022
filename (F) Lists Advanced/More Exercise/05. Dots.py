def correct_lab_bounds(row, col):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return True


def check_wall(row, col):
    if lab[row][col] in "-–":
        return True


def check_already_visit(row, col):
    if lab[row][col] == "v":
        return True


def find_exit(row, col):
    if lab[row][col] == ".":
        return True


def find_the_lab_path(row, col, lab):
    if correct_lab_bounds(row, col) or check_wall(row, col) or check_already_visit(row, col):
        return

    path_steps.append(1)

    if find_exit(row, col):
        max_connected_points.append(sum(path_steps))

    lab[row][col] = "v"
    find_the_lab_path(row, col + 1, lab)  # check right
    find_the_lab_path(row, col - 1, lab)  # check left
    find_the_lab_path(row + 1, col, lab)  # check up
    find_the_lab_path(row - 1, col, lab)  # check down


row = int(input())
lab = []
max_connected_points = [0]
for curr_row in range(row):
    lab.append(list(input().split()))

range_of_col = len(lab[0])

for row in range(len(lab)):
    for col in range(range_of_col):
        path_steps = []
        if not check_wall(row, col):
            find_the_lab_path(row, col, lab)


print(max(max_connected_points))