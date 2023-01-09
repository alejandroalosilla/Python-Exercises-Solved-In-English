# Ex070 - Create a program that reads the name and price of various products.
# The program should ask whether the user is going to continue or not.
# At the end, show:
#  A) What is the total amount spent on the purchase.
#  B) how many products cost more than R$1000.
#  C) what is the name of the cheapest product.

total_purchase = 0
over_1000 = 0
counter = 1
cheapest_product_name = ''
cheapest_product_price = 0

print(30 * '-')
print('         TEST STORE')
print(30 * '-')

while True:
    product_name = str(input('Product is name: ')).strip()
    price = float(input('Price: $'))
    option = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]

    total_purchase += price

    if price > 1000:
        over_1000 += 1
    if counter == 1:
        cheapest_product_name = product_name
        cheapest_product_price = price
    if price < cheapest_product_price:
        cheapest_product = price
        cheapest_product_name = product_name
    if option == 'N':
        break

    counter += 1

print('------- END OF PROGRAM! -------')
print(f'The total purchase was ${total_purchase:.2f}')
print(f'We have {over_1000} products costing over $1000.00')
print(f'The cheapest product was a {cheapest_product_name} that costs ${cheapest_product_price:.2f}')
