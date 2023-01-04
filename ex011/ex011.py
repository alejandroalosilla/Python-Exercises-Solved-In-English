#  Ex011 - Make a program that reads the width and height of a wall
# in meters, calculates its area and the amount of paint needed
# to paint it, knowing that each liter of paint paints an area of
# 2 square meters.

w_width = float(input('Wall width: '))
w_height = float(input('Wall height: '))

area = w_width * w_height
liters_to_paint = area / 2

print(f'Its wall has the dimension of {w_width:.2f}m x {w_height:.2f}m and its area is {area:.2f}m².')
print(f'To paint this wall, you will need {liters_to_paint:.2f}l of paint.')
