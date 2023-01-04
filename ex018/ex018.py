#  Ex018 - Make a program that reads any angle and shows on the screen
# the value of sine, cosine and tangent of that angle.

from math import sin, cos, tan, radians

angle = float(input('Enter the angle you want: '))

angle_in_radians = radians(angle)

sine = sin(angle_in_radians)
cosine = cos(angle_in_radians)
tangent = tan(angle_in_radians)

print(f'The angle of {angle} has a SINE of {sine:.2f}')
print(f'The angle of {angle} has a COSINE of {cosine:.2f}')
print(f'The angle of {angle} has a TANGENT of {tangent:.2f}')
