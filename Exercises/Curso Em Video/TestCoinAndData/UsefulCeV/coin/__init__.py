def increase(value = 0, increaseTax = 0, format=False):
    total = value + (value * (increaseTax / 100))
    return total if format is False else coin(total)

def decrease(value = 0, decreaseTax = 0, format=False):
    total = value - (value * (decreaseTax / 100))
    return total if format is False else coin(total)

def double(value = 0, format=False):
    total = value * 2
    return total if format is False else coin(total)  

def half(value = 0, format=False):
    total = value / 2
    return total if format is False else coin(total)     

def coin(value = 0, coin = '$'):
    return f'{coin}{value:>.2f}'.replace('.', ',')

def resume(value = 0, increaseTax = 0, decreaseTax = 0, format=False):
    print('-=' * 30)   
    print('RESUME OF PRICE'.center(30))
    print('-=' * 30)  
    print(f'Analyzed price: \t\t{coin(value)}')
    print(f'Double of the price: \t\t{double(value, True)}')
    print(f'Half of the price: \t\t{half(value, True)}')
    print(f'Increasing {increaseTax}% of the price: \t{increase(value, increaseTax, True)}')
    print(f'Decreasing {decreaseTax}% of the price: \t{increase(value, decreaseTax, True)}')
    print('-=' * 30)