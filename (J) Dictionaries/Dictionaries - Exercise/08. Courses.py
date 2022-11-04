courses = {}
command = input()
while command != 'end':
    course, name = command.split(' : ')

    if course not in courses:
        courses[course] = [name]

    elif course in courses:
        courses[course].append(name)

    command = input()

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    print('--', '\n-- '.join(students))