#  Ex109 - Modify the functions created in challenge #107 so that they accept
# one more parameter, informing whether the value returned by
# them will be formatted by the coin() function, developed in
# challenge 108.

import coin

p = float(input('Enter price: $'))
print(f'Half of {coin.currency(p)} is {coin.half(p, True)}')
print(f'The double of {coin.currency(p)} is {coin.double(p, True)}')
print(f'Increasing by 10% we get {coin.increase(p, True)}')
print(f'Decreasing 10%, we have {coin.decrease(p, True)}')
