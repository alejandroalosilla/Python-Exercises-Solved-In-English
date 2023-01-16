def half(v):
    v /= 2
    return v


def double(v):
    v *= 2
    return v


def increase(v):
    v += (0.1 * v)
    return v


def decrease(v):
    v -= (0.1 * v)
    return v


def currency(v):
    v = f'{v:.2f}'
    v = v.replace('.', ',')
    return f'${v}'
