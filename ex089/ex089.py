#  Ex089 - Create a program that reads the name and two grades of several
# students and stores them all in a composite list.
#  At the end, show the average of each one and allow the user to show
# the grades of each student individually.

from time import sleep

student_list = list()
data = list()

while True:
    data.append(str(input('Name: ')).strip())
    data.append(float(input('Grade 1: ')))
    data.append(float(input('Grade 2: ')))
    average = (data[1] + data[2]) / 2
    data.append(average)
    student_list.append(data[:])
    data.clear()

    option = ''
    while option != 'N' and option != 'Y':
        option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    if option == 'N':
        break
print(30 * '-=')
print('No. NOME         MÉDIA')
print(30 * '-')
for c in range(0, len(student_list)):
    print(f'{c:<4}{student_list[c][0]:<14}{student_list[c][3]:.1f}')
print(30 * '-')
while True:
    student = int(input('Show grades for which student?(999 to break): '))
    if student == 999:
        break
    print(f"{student_list[student][0]}'s grades: {student_list[student][1:3]}")
print('FINISHING...')
sleep(1)
print('<<< FINISHED >>>')
