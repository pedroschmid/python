valueOne = int(input('Type the first value: '))
valueTwo = int(input('Type the second value: '))
valueThree = int(input('Type the third value: '))

higher = valueOne
lower = valueOne

# higher value conditions
if higher < valueTwo:
    higher = valueTwo
elif higher < valueThree:
    higher = valueThree

# lower value conditions
if lower > valueTwo:
    lower = valueTwo
elif lower > valueThree:
    lower = valueThree

print(f'The highest value is {higher}')
print(f'The lowest value is {lower}')
