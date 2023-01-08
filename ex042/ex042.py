#  Ex042 - Redo CHALLENGE 035 of the triangles, adding the feature of
# showing what kind of triangle will be formed:
# - EQUILATERAL: all sides equal
# - ISOSCELES: two equal sides, one different
# - SCALENUM: all different sides

print(30 * '-=')
print('Triangle Analyzer')
print(30 * '-=')

a = float(input('First line segment: '))
b = float(input('Second line segment: '))
c = float(input('Third line segment: '))

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    if a == b == c:
        print('The segments above CAN FORM a SCALENE triangle!')
    elif a == b != c or a == c != b or c == b != a:
        print('The segments above CAN FORM a ISOSCELES triangle!')
    else:
        print('The segments above CAN FORM a SCALENUM triangle!')
else:
    print('The segments above CANNOT FORM a triangle!')
