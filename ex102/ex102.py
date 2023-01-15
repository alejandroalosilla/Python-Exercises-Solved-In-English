#  Ex102 - Create a program that has a factorial() function that receives two
# parameters: the first one that indicates the number to be calculated
# and another called show, which will be a logical value (optional)
# indicating whether the factorial calculation process will be
# shown on the screen .

def factorial(a, show=False):
    f = 1
    for c in range(a, 0, -1):
        f *= c
    if show is False:
        return f
    else:
        for c in range(a, 0, -1):
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
        return f


print(30 * '-')
print(factorial(5, True))
