from UsefulCeV import coin, data

price = data.readMoney('Type the price: $')
increaseTax = int(input('Type the increase tax: '))
decreaseTax = int(input('Type the decrease tax: '))

coin.resume(price, increaseTax, decreaseTax)