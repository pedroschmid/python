count = 0

for i in range(0,7):
    age = int(input(f'Type the age {i+1}: '))

    if age >= 18:
        count += 1

print(f'{count} peoples are legal age!')        