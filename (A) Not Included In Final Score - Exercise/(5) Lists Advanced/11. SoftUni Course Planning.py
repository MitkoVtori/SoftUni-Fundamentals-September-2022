def add(course: list, title: str):
    if title not in course:
        course.append(title)


def insert(course: list, title: str, index: int):
    if title not in course:
        course.insert(index, title)


def remove(course: list, title: str):
    if title in course:
        if f"{title}-Exercise" in course:
            course.remove(f"{title}-Exercise")
        course.remove(title)


def swap(course: list, first_title: str, second_title: str):
    if first_title in course and second_title in course:
        first_course_index = course.index(first_title)
        second_course_index = course.index(second_title)
        course[first_course_index], course[second_course_index] = course_list[second_course_index], course_list[first_course_index]
        index = course.index(second_title) + 1
        if index < len(course):
            if course[index] == f"{first_title}-Exercise":
                course.pop(index)
                index = course.index(first_title) + 1
                course.insert(index, f"{first_title}-Exercise")
        index = course.index(first_title) + 1
        if index < len(course):
            if course[index] == f"{second_title}-Exercise":
                course.pop(index)
                index = course.index(second_title) + 1
                course.insert(index, f"{second_title}-Exercise")


def exercise(course: list, title: str):
    if title in course and f"{title}-Exercise" not in course:
        index = course.index(title)
        course.insert(index + 1, f"{title}-Exercise")
    elif title not in course:
        course.append(title)
        course.append(f"{title}-Exercise")


course_list = input().split(', ')

while True:
    command = input().split(':')

    if command[0] == "course start":
        break

    lesson_title = command[1]

    if command[0] == 'Add':
        add(course_list, lesson_title)

    elif command[0] == "Insert":
        current_index = int(command[-1])
        insert(course_list, lesson_title, current_index)

    elif command[0] == "Remove":
        remove(course_list, lesson_title)

    elif command[0] == "Swap":
        second_lesson_title = command[-1]
        swap(course_list, lesson_title, second_lesson_title)

    elif command[0] == "Exercise":
        exercise(course_list, lesson_title)

for curr_index, lesson_name in enumerate(course_list):
    print(f"{curr_index + 1}.{lesson_name}")