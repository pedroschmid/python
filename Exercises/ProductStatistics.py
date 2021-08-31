totalPrice = 0
productsCount = 0
cheapestProductName = ''
cheapestProductValue = 10_000_000

while True:
    name = str(input('Type the product name: ')).strip().title()
    price = float(input('Type the product price: $'))

    totalPrice += price

    if price > 1000:
        productsCount += 1

    if price < cheapestProductValue:
        cheapestProductName = name

    anwser = str(input('Want to add more products? [Y/N]: ')).strip().upper()

    if anwser == 'N':
        break

print(f'Total price: ${totalPrice} | Products over $1000: {productsCount} | Cheapest product name: {cheapestProductName}')    