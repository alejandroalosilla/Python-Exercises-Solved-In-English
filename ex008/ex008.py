#  Ex008 - Write a program that reads a value in meters and
# displays it converted to centimeters and millimeters.

value = float(input('Enter a value in meters: '))

centimeters = value * 100
millimeters = value * 1000

print(f'The value {value}m in centimetres: {centimeters:.2f}cm')
print(f'The value {value}m in millimeters: {millimeters:.2f}mm')
