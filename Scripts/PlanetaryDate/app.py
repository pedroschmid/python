import socket
import os
import datetime
import math

os.system('COLOR 0')


def indexMenu():
    print(f'\033[1;31m-=' * 35 + '\033[m')

    print('''\033[1;33m

                     *       +
               '                  |
           ()    .-.,="``"=.    - o -
                 '=/_       \     |
              *   |  '=._    |                              
                   \     `=./`,        '
                .   '=.__.=' `='      *
       +                         +
            O      *        '       .
  ____        _                          _ _     
 / ___|  __ _| |_ _   _ _ __ _ __   __ _| (_)___ 
 \___ \ / _` | __| | | | '__| '_ \ / _` | | / __|
  ___) | (_| | |_| |_| | |  | | | | (_| | | \__ /
 |____/ \__,_|\__|\__,_|_|  |_| |_|\__,_|_|_|___/
                                                 
    \033[m''')

    print(f'\033[1;33m>Author: Sholomon\033[m')
    print(f'\033[1;33m>Version: 1.0\033[m')
    print(f'\033[1;33m>Apresentation: Welcome to Saturnalis, follow the instructions below!\033[m')


def chooseMenu():
    print()
    print(f'\033[1;31m-=' * 35 + '\033[m')
    print()

    print(f'\033[1;33m[0]\033[m - Exit the program')
    print(f'\033[1;33m[1]\033[m - Know which planet is ruling the earth right now')


#  Dates from the OS
currentHour = datetime.datetime.now().hour  # Hour
currentMinutes = datetime.datetime.now().minute  # Hour
currentWeekDay = datetime.datetime.now().weekday()  # Week Day

weekdayNameList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#  Data Structure => { {}, {} }
weekDaysPlanets = {
    'Day': {
        'Sunday': ['Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury',
                   'Moon', 'Saturn'],

        'Monday': ['Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter',
                   'Mars', 'Sun'],

        'Tuesday': ['Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus',
                    'Mercury', 'Moon'],

        'Wednesday': ['Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn',
                      'Jupiter', 'Mars'],

        'Thursday': ['Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun',
                     'Venus', 'Mercury'],

        'Friday': ['Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon',
                   'Saturn', 'Jupiter'],

        'Saturday': ['Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars',
                     'Sun', 'Venus']
    },

    'Night': {
        'Sunday': ['Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus',
                   'Mercury'],

        'Monday': ['Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn',
                   'Jupiter'],

        'Tuesday': ['Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun',
                    'Venus'],

        'Wednesday': ['Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury',
                      'Moon', 'Saturn'],

        'Thursday': ['Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter',
                     'Mars', 'Sun'],

        'Friday': ['Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus',
                   'Mercury', 'Moon'],

        'Saturday': ['Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars',
                     'Sun', 'Venus']
    }
}

indexMenu()

while True:
    chooseMenu()
    menuChoose = int(input(f'\033[1;33m==> \033[m'))

    if menuChoose == 0:
        print('\033[1;31mThanks for using the program, exiting ...\033[m')
        break
    elif menuChoose == 1:
        while True:
            try:
                currentSunRise = float(input('What time did the sun rise? \033[1:31m[TYPE FLOAT NUMBERS EX: 5.30 FOR SUNRISE AT 5:30] \033[m'))
                currentSunSet = float(input('What time did the sun set? \033[1:31m[TYPE FLOAT NUMBERS EX: 18.30 FOR SUNSET AT 18:30] \033[m'))

                #  Transforms datetime into float
                timeHM = currentHour + (currentMinutes / 100)

                #  if/else to check if is night or day
                if currentSunRise < currentHour < currentSunSet:
                    dayStatus = 1
                    planetaryHour = math.trunc(timeHM - currentSunRise)
                    planetaryDate = weekDaysPlanets['Day'][weekdayNameList[currentWeekDay]][planetaryHour]
                else:
                    dayStatus = 0
                    planetaryHour = math.trunc(timeHM - currentSunSet)
                    planetaryDate = weekDaysPlanets['Night'][weekdayNameList[currentWeekDay]][planetaryHour]

            except KeyboardInterrupt:
                print(f'\n\033[1;31ERROR! THE USER DID NOT TYPE ANYTHING\033[m')

            else:
                if dayStatus == 1:
                    dayStatus = 'Day'
                    print(f'\n\033[1;34mDay Status: {dayStatus}\033[m\n\033[1;34mRuling planet: {planetaryDate}\033[m')
                else:
                    dayStatus = 'Night'
                    print(f'\n\033[1;34mDay Status: {dayStatus}\033[m\n\033[1;34mRuling planet: {planetaryDate}\033[m')

            finally:
                whileChoose = str(input('\nWant to enter another time for sunrise and sunset? [Y/N]\n\033[1;33m==> \033[m')).upper()[0]

            if whileChoose == 'N':
                break
            else:
                continue

