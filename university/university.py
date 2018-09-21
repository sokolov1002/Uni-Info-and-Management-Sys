class University:

    def __init__(self):
        self.name = 'Varna University of Management'
        self.president = 'Prof. Todor Radev'
        self.address = '13 A Oborishte Str. 9000'
        self.city = 'Varna'
        self.country = 'Bulgaria'
        self.majors = [
            {'Bachelor': 'Business Administration'},
            {'Bachelor': 'International Business Management'},
            {'Bachelor': 'Marketing and Management of Tourist Services'},
            {'Bachelor': 'Marketing and Management'},
            {'Bachelor': 'Hospitality Management'},
            {'Bachelor': 'Software Engineering'},
            {'Bachelor': 'Gastronomy and Culinary Arts'},
            {'Bachelor': 'International Finance and Trade'},
            {'Bachelor': 'Business Information Systems'},
            {'Bachelor': 'Hospitality and Culinary Arts'},
            {'Master': 'Business Administration'},
            {'Master': 'International Hospitality and Tourism Management'}
        ]
        self.students = []
        self.teachers = []

    def info(self):
        print()
        print(self.name)
        print(self.address + '' + self.city + '' + self.country)
        print(self.president)
        print()

    def show_majors(self):
        print()
        choice = int(input('(1) Bachelor (2) Master : '))
        if choice == 1:
            print()
            counter = 1
            for major in self.majors:
                for k, v in major.items():
                    if k == 'Bachelor':
                        print('{}. {}'.format(counter, v))
                        counter += 1
        elif choice == 2:
            print()
            counter = 1
            for major in self.majors:
                for k, v in major.items():
                    if k == 'Master':
                        print('{}. {}'.format(counter, v))
                        counter += 1
        print()

    def add_student(self, student):
        print()
        self.students.append(student)
        print()

    def search_student(self, number):
        print()
        for student in self.students:
            if number == student.student_number:
                print('Information about student {}: '.format(number))
                student.info()
                break
        print()

    def add_teacher(self, teacher):
        print()
        self.teachers.append(teacher)
        print()
