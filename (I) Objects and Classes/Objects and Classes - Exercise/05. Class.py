class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []
        self.average_grade = 0

    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)
            self.average_grade = sum(self.grades) / len(self.grades)

    def get_average_grade(self):
        return self.average_grade

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.average_grade:.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)