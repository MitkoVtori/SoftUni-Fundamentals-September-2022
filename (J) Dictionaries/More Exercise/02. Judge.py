command = input()

students_dictionary = {"user": {}, "contest": {}}
user_d = "user"
contest_d = "contest"

while command != "no more time":
    user_name, contest, points = command.split(" -> ")
    points = int(points)
    if contest not in students_dictionary[contest_d]:
        students_dictionary[contest_d][contest] = {}

    if user_name not in students_dictionary[contest_d][contest]:
        students_dictionary[contest_d][contest][user_name] = 0

    if user_name not in students_dictionary[user_d]:
        students_dictionary[user_d][user_name] = 0

    if user_name in students_dictionary[user_d] and students_dictionary[user_d][user_name] == points:
        students_dictionary[user_d][user_name] += points

    if students_dictionary[contest_d][contest][user_name] < points:
        students_dictionary[user_d][user_name] += points - students_dictionary[contest_d][contest][user_name]
        students_dictionary[contest_d][contest][user_name] = points

    command = input()


def show_result():
    for contest in students_dictionary[contest_d]:
        print(f"{contest}: {len(students_dictionary[contest_d][contest])} participants")
        for pos, (name, points) in enumerate(
                sorted(students_dictionary[contest_d][contest].items(), key=lambda item: (-item[1], item[0])), 1):
            print(f"{pos}. {name} <::> {points}")
    print("Individual standings:")
    for pos, (name, points) in enumerate(
            sorted(students_dictionary[user_d].items(), key=lambda item: (-item[1], item[0])), 1):
        print(f"{pos}. {name} -> {points}")


show_result()