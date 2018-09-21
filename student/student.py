from random import randint


class Student:

    grades = []

    def __init__(self, first_name, last_name, age, major):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.major = major
        self.user_name = self.first_name[:3].lower() + '_' + self.last_name[:3].lower() + '_' + self.age
        self.student_number = randint(1000000, 2000000)

    def info(self):
        print()
        print('First name: ', self.first_name)
        print('Last name: ', self.last_name)
        print('Age: ', self.age)
        print('Major: ', self.major)
        print()

    def check_grades(self, major):
        for grade in self.grades:
            if major == grade[0]:
                print(grade[1])
            else:
                continue
