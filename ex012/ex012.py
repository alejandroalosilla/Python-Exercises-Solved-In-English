#  Ex012 - Write an algorithm that reads the price of a product and
# displays its new price, with a 5% discount.

price = float(input('How much is the product price? $'))
new_price = price - (0.05 * price)

print(f'The product that cost ${price:.2f}, in the 5% discount promotion, will cost ${new_price:.2f}.')
