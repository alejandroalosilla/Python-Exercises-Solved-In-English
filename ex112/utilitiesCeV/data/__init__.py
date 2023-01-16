def readmoney(v):
    v = str(input(v)).strip().replace(',', '.')
    while v.isalpha() is True or v == '':
        print(f'\033[31mERROR! "{v}" is an invalid price!\033[m')
        v = str(input('Enter price: $')).strip().replace(',', '.')
    return float(v)
