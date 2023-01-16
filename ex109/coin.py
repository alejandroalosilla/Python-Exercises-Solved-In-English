def half(v, c=False):
    v /= 2
    if c is True:
        return currency(v)
    else:
        return v


def double(v, c=False):
    v *= 2
    if c is True:
        return currency(v)
    else:
        return v


def increase(v, c=False):
    v += (0.1 * v)
    if c is True:
        return currency(v)
    else:
        return v


def decrease(v, c=False):
    v -= (0.1 * v)
    if c is True:
        return currency(v)
    else:
        return v


def currency(v):
    v = f'{v:.2f}'
    v = v.replace('.', ',')
    return f'${v}'
