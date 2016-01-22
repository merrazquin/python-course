import statistics 
def add_grade(gradebook, studentName, grade):
    print('Adding grade...')
    try:
        gradebook[studentName].append(grade)
    except KeyError:
        gradebook[studentName] = [grade]

def remove_student(gradebook, studentName):
    print('Removing student...')
    try:
        del gradebook[studentName]
    except KeyError:
        print('The user',studentName,'does not exist in the gradebook')

def student_average_grades(gradebook, studentName):
    print('Calculating average...')
    try:
        grades = gradebook[studentName]
        print(statistics.mean(grades))
    except KeyError:
        print('The user',studentName,'does not exist in the gradebook')
