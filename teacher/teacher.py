from random import randint


class Teacher:

    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.user_name = self.first_name[:3].lower() + '_' + self.last_name[:3].lower()
        self.teacher_number = randint(1000, 9999)

    def write_grade(self, student, grade):
        student.grades.append({self.major: grade})
