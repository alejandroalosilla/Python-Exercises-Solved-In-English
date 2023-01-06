#  Ex040 - Create a program that reads two grades from a student and
# calculates their average, showing a message at the end,
# according to the average achieved:
# - Average below 5.0: FAILED
# - Average between 5.0 and 6.9: RECOVERY
# - Average 7.0 or higher: PASSED

first_grade = float(input('First grade: '))
second_grade = float(input('Second grade: '))

average = (first_grade + second_grade) / 2

if average < 5:
    print(f'With grades {first_grade:.1f} and {second_grade:.1f}, the student average is {average:.1f}.')
    print('The student is FAILED.')
elif 7 < average >= 5:
    print(f'With grades {first_grade:.1f} and {second_grade:.1f}, the student average is {average:.1f}.')
    print('The student is in RECOVERY.')
else:
    print(f'With grades {first_grade:.1f} and {second_grade:.1f}, the student average is {average:.1f}.')
    print('The student is APPROVED.')
