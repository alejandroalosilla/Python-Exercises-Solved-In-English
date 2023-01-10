#  Ex076 - Create a program that has a single tuple with product names and
# their respective prices, in sequence.
#  At the end, show a price list, organizing the data in tabular form.

# colors:
#         yellow[0]:   green[1]:    blue[2]:
color = ('\033[33m', '\033[32m', '\033[36m')

products = ('Pencil', 1.75, 'Eraser', 2.00, 'Notebook', 15.90, 'Case', 25.00, 'Protractor', 4.20,
            'Compass', 9.99, 'Backpack', 120.32, 'Pens', 22.30, 'Book', 34.90)

print(50 * f'{color[2]}-')
print('                PRICE LISTING')
print(50 * '-')

for c in range(0, len(products)):
    if c % 2 == 0:
        print(f'{color[0]}{products[c]:.<40}$ ', end='')
    else:
        print(f'{color[1]}{products[c]:.2f}')
print(50 * f'{color[2]}-')
