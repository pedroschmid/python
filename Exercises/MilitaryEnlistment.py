age = int(input('Type your age: '))
enlistmentTime = age - 18

if age == 18:
    print('The time has come to enlist!')
elif age > 18:
    print(f'You are late in {enlistmentTime} years for enlistment!')
elif age < 18:
    print('You do not have to enlist yet!')