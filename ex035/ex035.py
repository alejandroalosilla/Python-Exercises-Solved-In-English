#  Ex035 - Develop a program that reads the length of three lines and
# tells the user whether they can form a triangle.

print(30 * '-=')
print('Triangle Analyzer')
print(30 * '-=')

a = float(input('First line segment: '))
b = float(input('Second line segment: '))
c = float(input('Third line segment: '))

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('The segments above CAN FORM a triangle!')
else:
    print('The segments above CANNOT FORM a triangle!')
