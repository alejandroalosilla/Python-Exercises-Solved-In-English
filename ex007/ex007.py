#  Ex007 - Develop a program that reads a student's two grades,
# calculates and displays their average.

f_grade = float(input("Student's first grade: "))
s_grade = float(input("Student's second grade: "))

average = (f_grade + s_grade) / 2

print(f'The average between {f_grade:.1f} and {s_grade:.1f} equals {average:.1f}.')
