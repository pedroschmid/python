scoreOne = float(input('Type the first exam score: '))
scoreTwo = float(input('Type the second exam score: '))

average = scoreOne + scoreTwo / 2

if average > 7.0:
    print(f'Your average is {average}, you passed!')
elif 5.0 <= average <= 6.9:
    print(f'Your average is {average}, you are recovering')
else:
    print(f'Your average is {average}, you failed')