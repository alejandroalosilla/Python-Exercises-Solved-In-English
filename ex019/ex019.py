#  Ex019 - A teacher wants to draw one of his four students to erase
# the blackboard. Make a program that helps him, reading the
# students' names and writing the name of the chosen one on
# the screen.

from random import choice

name_student_1 = str(input('First student: '))
name_student_2 = str(input('Second student: '))
name_student_3 = str(input('Third student: '))
name_student_4 = str(input('Fourth student: '))

list_name = [name_student_1, name_student_2, name_student_3, name_student_4]

teacher_choice = choice(list_name)
print(f'The chosen student was {teacher_choice}')
