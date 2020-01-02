def factorial(number, show):
    factorialSumm = 1
    
    if show == True:
        for i in range(number, 0, -1):
            factorialSumm *= i
            print(f'{i} x ', end='')
        return f'= {factorialSumm}'    
    else:
        for i in range(number, 0, -1):
            factorialSumm *= i
        return f'{number}! = {factorialSumm}'

print('=-' * 20)

number = int(input('Type the number do you want to know the factorial: '))
choose = int(input('Want to show the proccess? [0 False/1 True] '))

if choose == 0:
    show = False
else:
    show = True    

print(factorial(number, show))

print('=-' * 20)