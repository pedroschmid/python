higherAge = 0
countAge = 0
ageAverage = 0

for i in range(0,4):
    name = str(input(f'Type the name of person [{i+1}]: ')).strip().upper()
    age = int(input(f'Type the age of person [{i+1}]: '))
    sex = str(input(f'Type the sex of person [{i+1}]: ')).strip().upper()

    print('')

    if sex == 'MALE' and age > higherAge:
        higherAge = age

    if sex == 'FEMALE' and age < 20:
        countAge += 1 

    ageAverage += age       

print(f'Average Age: {ageAverage} | Older Man: {higherAge} | Women Under 20y: {countAge}')