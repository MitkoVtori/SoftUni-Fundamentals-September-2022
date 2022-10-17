students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_attendances = 0
max_bonus_points = 0

for attendances in range(students):
    student_attendances = int(input())
    bonus = student_attendances / lectures * (5 + additional_bonus)
    if student_attendances >= max_attendances:
        max_attendances = student_attendances
    if bonus >= max_bonus_points:
        max_bonus_points = bonus

max_attendances = round(max_attendances)
max_bonus_points = round(max_bonus_points)

print(f"Max Bonus: {max_bonus_points}.")
print(f"The student has attended {max_attendances} lectures.")