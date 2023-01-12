#  Ex096 - Make a program that has a function called area(), which receives
# the dimensions of a rectangular terrain (width and length) and shows
# the area of the terrain.


def area():
    print(' Terrain Area')
    print(14 * '-')
    width = float(input('Width (m): '))
    length = float(input('Length (m): '))
    print(f'The land area is {(width * length):.1f}m²')


area()
