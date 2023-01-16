#  Ex111 - Create a package called utilitiesCeV that has two built-in modules
# called coin and data.
#  Transfer all functions used in challenges 107, 108 and 109 to the
# first package and keep everything working.

from utilitiesCeV import coin

p = float(input('Enter price: $'))
coin.summary(p, 15, 15)
