n = int(input())
# EMPTY LIST:
courses = list() # or []

for course in range(n):
    curr_course = input()
    courses.append(curr_course) # adding the course to the list
print(courses)
