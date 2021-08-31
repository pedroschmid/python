houseValue = float(input('Type the house value: $'))
buyerSalary = float(input('Type the buyer salary: $'))
years = int(input('Type how many years you will pay: '))

monthlyInstallment = houseValue / (years * 12)
minimumInstallment = buyerSalary * .30

if monthlyInstallment <= minimumInstallment:
    print('The loan was approved!')
else:
    print('The loan was not approved!')