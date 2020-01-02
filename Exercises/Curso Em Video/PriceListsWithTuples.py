tupla = (
    'Pencil', 1.75,
    'Eraser', 2.00,
    'Book', 15.90,
    'Case', 25.00,
    'Compass', 9.99,
    'Backpack', 120.32,
    'Pen', 3.00
)

print('=' * 40)

for name, price in zip(tupla[0::2], tupla[1::2]):
    print(f'{name:.<30} $ {price}')
        
print('=' * 40)        