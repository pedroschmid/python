carSpeed = float(input('Type the car speed: '))
trafficTicket = 0

if carSpeed > 80:
    trafficTicket = (carSpeed - 80) * 7.00
    print(f'You have been fined, the amount of the fine is ${trafficTicket}')
elif carSpeed == 80:
    print('You are at the speed limit, please reduce!')
else:
    print('You are at normal speed!')