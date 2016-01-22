import grades
import getpass

gradebook = {}

default_user = 'user'
default_pass = 'pass'

logged_in = False

def prompt():
    print("""
    Welcome to Grade Central

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit

    """)
    main_loop()

def main_loop():
    action = input('What would you like to do today? (Enter a number) ')
    take_action(action)


def take_action(action):
    if action == '4':
        print('Bye')
        return

    if action == 'help':
        prompt()
    elif action == '1':
        student_name = input('Student Name: ')
        grade = input('Grade: ')
        grades.add_grade(gradebook, student_name, float(grade))
    elif action == '2':
        student_name = input('Student Name: ')
        grades.remove_student(gradebook, student_name)
    elif action == '3':
        student_name = input('Student Name: ')
        grades.student_average_grades(gradebook, student_name)
    else:
        print('Unrecognized command',action);

    print(gradebook)
    main_loop()

def login():
    while True:
        username = input('Username: ')
        password = getpass.getpass('Password: ')

        if username != default_user or password != default_pass:
            print('Invalid credentials');
        else:
            prompt()
            break

login()
