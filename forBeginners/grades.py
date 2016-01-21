import statistics 
def addGrade(gradebook, studentName, grade):
    print('Adding grade...')
    try:
        gradebook[studentName].append(grade)
    except:
        gradebook[studentName] = [grade]

def removeStudent(gradebook, studentName):
    print('Removing student...')
    try:
        del gradebook[studentName]
    except:
        print('The user',studentName,'does not exist in the gradebook')

def studentAverageGrades(gradebook, studentName):
    print('Calculating average...')
    try:
        grades = gradebook[studentName]
        print(statistics.mean(grades))
    except:
        print('The user',studentName,'does not exist in the gradebook')
