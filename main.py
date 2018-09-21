from db_connect import Database
from university.university import University
from student.student import Student
from teacher.teacher import Teacher

vum_db = Database()
vum = University()

vum_db.cursor_execute('SHOW TABLES')
results = vum_db.cursor.fetchall()
results_list = [item[0] for item in results]

if 'teachers' in results_list:
    pass
    # print(table1, 'was found!')
else:
    vum_db.cursor_execute('CREATE TABLE teachers (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), major VARCHAR(255), usr VARCHAR(255), pass VARCHAR(255))')
if 'students' in results_list:
    pass
    # print(table2, 'was found!')
else:
    vum_db.cursor_execute('CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), age INT, major VARCHAR(255), usr VARCHAR(255), pass VARCHAR(255))')


main_menu = True
while main_menu:
    print()
    print('School Information System vol.1')
    print()
    print("""Please, choose an option from the menu:

    (1) Login/Register for teachers
    (2) Login/Register for students
    (3) General information
    (4) Exit

    """)
    choice_main = int(input('Enter (1), (2), (3) or (4): '))
    if choice_main == 1:
        print()
        teacher_menu = True
        while teacher_menu:
            print("""Please, choose an option from the menu:

   (1) Login
   (2) Register
   (3) Exit

                           """)
            choice_teachers = int(input('Enter (1), (2), (3) or (4): '))
            if choice_teachers == 1:
                pass
            elif choice_teachers == 2:
                print()
                file = open('teacher/tdb.txt', 'a')
                first_name = input('Enter your first name: ')
                last_name = input('Enter your last name: ')
                major = input('Enter your major: ')
                teacher = Teacher(first_name, last_name, major)
                file.write('{},{},{},usr:{},pass:{}\n'.format(first_name,
                                                              last_name,
                                                              major,
                                                              teacher.user_name,
                                                              teacher.teacher_number))
                file.close()
                print()
                print('Registration completed!')
                print()
                print('Your login details are:')
                print()
                print('username: ', teacher.user_name)
                print('password: ', teacher.teacher_number)
                vum.add_teacher(teacher)
                sql = 'INSERT INTO teachers (fname, lname, major, usr, pass) VALUES (%s, %s, %s, %s, %s)'
                data = (first_name, last_name, major, teacher.user_name, teacher.teacher_number)
                vum_db.cursor_execute(sql, data)
            elif choice_teachers == 3:
                print()
                print('Goodbye!')
                teacher_menu = False
    elif choice_main == 2:
        print()
        student_menu = True
        while student_menu:
            print("""Please, choose an option from the menu:

    (1) Login
    (2) Register
    (3) Exit

                """)
            choice_students = int(input('Enter (1), (2) or (3): '))
            if choice_students == 1:
                pass
            elif choice_students == 2:
                print()
                file = open('student/sdb.txt', 'a')
                first_name = input('Enter your first name: ')
                last_name = input('Enter your last name: ')
                age = input('Enter your age: ')
                major = input('Enter your major: ')
                student = Student(first_name, last_name, age, major)
                file.write('{},{},{},{},usr:{},pass:{}\n'.format(first_name,
                                                                 last_name,
                                                                 age,
                                                                 major,
                                                                 student.user_name,
                                                                 student.student_number))
                file.close()
                print()
                print('Registration completed!')
                print()
                print('Your login details are:')
                print()
                print('username: ', student.user_name)
                print('password: ', student.student_number)
                vum.add_student(student)
                sql = 'INSERT INTO students (fname, lname, age, major, usr, pass) VALUES (%s, %s, %s, %s, %s, %s)'
                data = (first_name, last_name, age, major, student.user_name, student.student_number)
                vum_db.cursor_execute(sql, data)
            elif choice_students == 3:
                print()
                print('Goodbye!')
                student_menu = False
    elif choice_main == 3:
        print()
        information_menu = True
        while information_menu:
            print("""Please, choose an option from the menu:
    
    (1) University information
    (2) List majors
    (3) Student information
    (4) Exit
    
                """)
            choice_information = int(input('Enter (1), (2), (3) or (4): '))
            if choice_information == 1:
                vum.info()
            elif choice_information == 2:
                vum.show_majors()
            elif choice_information == 3:
                student_number = int(input('Enter student number to search: '))
                vum.search_student(student_number)
            elif choice_information == 4:
                print('Goodbye!')
                information_menu = False
    elif choice_main == 4:
        print('Goodbye!')
        main_menu = False
