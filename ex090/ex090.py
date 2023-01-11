#  Ex090 - Make a program that reads a student's name and average, also saving
# the situation in a dictionary.
#  At the end, show the contents of the structure on the screen.

student_dict = dict()

student_dict['Name'] = str(input('Name: ')).strip().capitalize()
student_dict['Grade'] = float(input('Média: '))
if student_dict['Grade'] >= 7:
    student_dict['Status'] = '\033[32mApproved'
else:
    student_dict['Status'] = '\033[31mDisapproved'

print(30 * '-=')
for k, v in student_dict.items():
    print(f'- {k} equals {v}')
