student_grades = {}
languages_dictionary = {}


def max_grade(name, curr_grade):
    if name in student_grades:
        if curr_grade >= student_grades[name]:
            student_grades[name] = curr_grade
    elif name not in student_grades:
        student_grades[name] = curr_grade


def banned(name):
    if name in student_grades:
        del student_grades[name]


def submissions(used_language):
    if used_language in languages_dictionary:
        languages_dictionary[used_language] += 1
        return
    languages_dictionary[used_language] = 1


while True:
    command = input()

    if command == 'exam finished':
        break

    indices = command.split('-')

    if indices[1] == 'banned':
        banned(indices[0])
        continue

    username, language, grade = command.split('-')
    grade = int(grade)

    max_grade(username, grade)
    submissions(language)

print('Results:')
for student, grade in student_grades.items():
    print(student, '|', grade)
print('Submissions:')
for curr_language, submissions in languages_dictionary.items():
    print(curr_language, '-', submissions)