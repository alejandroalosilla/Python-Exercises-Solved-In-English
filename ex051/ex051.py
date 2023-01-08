#  Ex051 - Develop a program that reads the first term and ratio of an AP.
# At the end, show the first 10 terms of this progression.

print(20 * '=')
print('10 TERMS OF AN ARITHMETIC PROGRESSION')
print(20 * '=')

first = int(input('First term: '))
ratio = int(input('Ratio: '))
t1 = first

for c in range(0, 10):
    if c == 9:
        print(f'{t1} -> END')
    else:
        print(f'{t1} ->', end=' ')
    t1 += ratio
