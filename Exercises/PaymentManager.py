import os

os.system('cls' if os.name == 'nt' else 'clear')

normalPrice = float(input('Type the product price: '))
paymentMethod = str(input('Type the payment method (money or card): ')).strip().upper()

if paymentMethod == 'MONEY':
    totalPrice = normalPrice - (normalPrice * 0.1)   
    print(f'The amount to be paid is ${totalPrice}') 
else:
    paymentCondition = str(input('Type the payment condition: (cash or divided)')).strip().upper()

    if paymentCondition == 'CASH':
        totalPrice = normalPrice - (normalPrice * 0.05)
        print(f'The amount to be paid is ${totalPrice}') 
    elif paymentCondition == '2X':
        totalPrice = normalPrice
        print(f'The amount to be paid is ${totalPrice}') 
    else:
        totalPrice = normalPrice + (normalPrice * 0.2)
        print(f'The amount to be paid is ${totalPrice}')         
