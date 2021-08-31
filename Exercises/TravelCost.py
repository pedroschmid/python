distance = float(input('Type the trip distance: '))
travelCost = 0

if distance > 200:
    travelCost = distance * 0.45
    print(f'The travel cost is ${travelCost}')
else:
    travelCost = distance * 0.50
    print(f'The travel cost is ${travelCost}')
