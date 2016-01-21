import grades
import getpass

gradebook = {}

defaultUser = 'user'
defaultPass = 'pass'

def login():
    username = input('Username: ')
    try:
        password = getpass.getpass('Password: ')
    except:
        #shhhh it's ok
        print('')

    if(username != defaultUser or password != defaultPass):
        print('invalid credentials')
        login()
    else:
        prompt()

def prompt():
    print('Welcome to Grade Central')
    print('')
    print('[1] - Enter Grades')
    print('[2] - Remove Student')
    print('[3] - Student Average Grades')
    print('[4] - Exit')

    print('')
    mainLoop()

def mainLoop():
    action = input('What would you like to do today? (Enter a number) ')
    takeAction(action)


def takeAction(action):
    if(action == '4'):
        print('Bye')
        return

    if(action == 'help'):
        prompt()
    elif(action == '1'):
        studentName = input('Student Name: ')
        grade = input('Grade: ')
        grades.addGrade(gradebook, studentName, float(grade))
    elif(action == '2'):
        studentName = input('Student Name: ')
        grades.removeStudent(gradebook, studentName)
    elif(action == '3'):
        studentName = input('Student Name: ')
        grades.studentAverageGrades(gradebook, studentName)
    else:
        print('Unrecognized command',action);

    print(gradebook)
    mainLoop()

login()
