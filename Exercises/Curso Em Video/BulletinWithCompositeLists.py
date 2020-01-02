studentSituation = {}

studentSituation['name'] = str(input('Type your name: '))
studentSituation['average'] = float(input('Type your average: '))

if studentSituation['average'] >= 7:
    studentSituation['status'] = 'Approved'
else:
    studentSituation['status'] = 'Disapproved'

print('-=' * 30)
for k, v in studentSituation.items():
    print(f'{k}: {v}')
print('-=' * 30)