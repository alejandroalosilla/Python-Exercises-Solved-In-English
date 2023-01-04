#  Ex020 - The same teacher from challenge 019 wants to raffle the order
# in which students' work will be presented.
#  Make a program that reads the names of the four students and
# shows the order drawn.

from random import shuffle

name_student_1 = str(input('First student: '))
name_student_2 = str(input('Second student: '))
name_student_3 = str(input('Third student: '))
name_student_4 = str(input('Fourth student: '))

list_name = [name_student_1, name_student_2, name_student_3, name_student_4]
shuffle(list_name)

print('The order of presentation will be: ')
print(list_name)
