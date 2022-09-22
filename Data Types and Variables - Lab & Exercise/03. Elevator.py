from math import ceil

people = int(input())
capacity = int(input())

if capacity != 0:
  courses = ceil(people/capacity)
print(courses)
