import math

height = float(input('Type your height: '))
weight = float(input('Type your weight: '))
imc = weight / pow(height, 2)

if imc < 18.5:
    print(f'Your IMC is {imc}, you are under weight!')
elif 18.5 < imc < 25:
    print(f'Your IMC is {imc}, you are at ideal weight!')
elif 25 < imc < 30:
    print(f'Your IMC is {imc}, you are over weight!')
elif 30 < imc < 40:
    print(f'Your IMC is {imc}, you have obesity I!')
else:
    print(f'Your IMC is {imc}, you have morbid obesity!')
