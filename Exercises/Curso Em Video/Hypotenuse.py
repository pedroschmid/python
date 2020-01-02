import math

a = int(input('Type the "A²" value: '))
b = int(input('Type the "B²" value: '))

hypotenuse = (a ** 2) + (b ** 2)
hypotenuse = math.sqrt(hypotenuse)

print(f'The hypotenuse of A² being {a} and B² being {b} is {hypotenuse} ')