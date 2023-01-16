def half(v):
    v /= 2
    return currency(v)


def double(v):
    v *= 2
    return currency(v)


def increase(v, p1):
    v += ((p1 / 100) * v)
    return currency(v)


def decrease(v, p2):
    v -= ((p2 / 100) * v)
    return currency(v)


def currency(v):
    v = f'{v:.2f}'
    v = v.replace('.', ',')
    return f'${v}'


def summary(a, i, d):
    print(30 * '-')
    print('        VALUE SUMMARY')
    print(30 * '-')
    print(f'Analyzed price:     {currency(a)}')
    print(f'Half-price:         {half(a)}')
    print(f'Double the price:   {double(a)}')
    print(f'{i}% increase:       {increase(a, i)}')
    print(f'{d}% Decrease:       {decrease(a, d)}')
    print(30 * '-')
