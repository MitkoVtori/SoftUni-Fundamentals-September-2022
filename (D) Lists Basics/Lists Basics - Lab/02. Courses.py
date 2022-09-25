number_courses = int(input())
# EMPTY LIST:
courses = list() # or []

for course in range(number_courses):
    curr_course = input()
    courses.append(curr_course) # adding the course to the list
print(courses)
