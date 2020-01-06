def leapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def updateDictionary(dictionary, content):
    dictionary.clear()
    dictionary.update(content)


# date[currentMonth][2][weekdayNameList[currentWeekDay]] // Key for reach the current date

weekdayNameList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
planets = ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn']

#  [ [month, days, {week days}], ]
date = [
    ['January', 31, {
        'Sunday': [5, 12, 19, 26],
        'Monday': [6, 13, 20, 27],
        'Tuesday': [7, 14, 21, 28],
        'Wednesday': [8, 15, 22, 29],
        'Thursday': [2, 9, 16, 23, 30],
        'Friday': [3, 10, 17, 24, 31],
        'Saturday': [4, 11, 18, 25]
    }],
    ['February', 28, {
        'Sunday': [3, 10, 17, 24],
        'Monday': [4, 11, 18, 25],
        'Tuesday': [5, 12, 19, 26],
        'Wednesday': [6, 13, 20, 27],
        'Thursday': [7, 14, 21, 28],
        'Friday': [1, 8, 15, 22],
        'Saturday': [2, 9, 16, 23]
    }],
    ['March', 31, {
        'Sunday': [1, 8, 15, 22, 29],
        'Monday': [2, 9, 16, 23, 30],
        'Tuesday': [3, 10, 17, 24, 31],
        'Wednesday': [4, 11, 18, 25],
        'Thursday': [5, 12, 19, 26],
        'Friday': [6, 13, 20, 27],
        'Saturday': [7, 14, 21, 28]
    }],
    ['April', 30, {
        'Sunday': [5, 12, 19, 26],
        'Monday': [6, 13, 20, 27],
        'Tuesday': [7, 14, 21, 28],
        'Wednesday': [1, 8, 15, 22, 29],
        'Thursday': [2, 9, 16, 23, 30],
        'Friday': [3, 10, 17, 24],
        'Saturday': [4, 11, 18, 25]
    }],
    ['May', 31, {
        'Sunday': [3, 10, 17, 24, 31],
        'Monday': [4, 11, 18, 25],
        'Tuesday': [5, 12, 19, 26],
        'Wednesday': [6, 13, 20, 27],
        'Thursday': [7, 14, 21, 28],
        'Friday': [1, 8, 15, 22, 29],
        'Saturday': [2, 9, 16, 23, 30]
    }],
    ['June', 30, {
        'Sunday': [7, 14, 21, 28],
        'Monday': [1, 8, 15, 22, 29],
        'Tuesday': [2, 9, 16, 23, 30],
        'Wednesday': [3, 10, 17, 24],
        'Thursday': [4, 11, 18, 25],
        'Friday': [5, 12, 19, 26],
        'Saturday': [6, 13, 20, 27]
    }],
    ['July', 31, {
        'Sunday': [5, 12, 19, 26],
        'Monday': [6, 13, 20, 27],
        'Tuesday': [7, 14, 21, 28],
        'Wednesday': [1, 8, 15, 22, 29],
        'Thursday': [2, 9, 16, 23, 30],
        'Friday': [3, 10, 17, 24, 31],
        'Saturday': [4, 11, 18, 25]
    }],
    ['August', 31, {
        'Sunday': [2, 9, 16, 23, 30],
        'Monday': [3, 10, 17, 24, 31],
        'Tuesday': [4, 11, 18, 25],
        'Wednesday': [5, 12, 19, 26],
        'Thursday': [6, 13, 20, 27],
        'Friday': [7, 14, 21, 28],
        'Saturday': [1, 8, 15, 22, 29]
    }],
    ['September', 30, {
        'Sunday': [6, 13, 20, 27],
        'Monday': [7, 14, 21, 28],
        'Tuesday': [8, 15, 22, 29],
        'Wednesday': [2, 9, 16, 23, 30],
        'Thursday': [3, 10, 17, 24, 31],
        'Friday': [4, 11, 18, 25],
        'Saturday': [5, 12, 19, 26]
    }],
    ['October', 31, {
        'Sunday': [4, 11, 18, 25],
        'Monday': [5, 12, 19, 26],
        'Tuesday': [6, 13, 20, 27],
        'Wednesday': [7, 14, 21, 28],
        'Thursday': [1, 8, 15, 22, 29],
        'Friday': [2, 9, 16, 23, 30],
        'Saturday': [3, 10, 17, 24, 31]
    }],
    ['November', 30, {
        'Sunday': [1, 8, 15, 22, 29],
        'Monday': [2, 9, 16, 23, 30],
        'Tuesday': [3, 10, 17, 24],
        'Wednesday': [4, 11, 18, 25],
        'Thursday': [5, 12, 19, 26],
        'Friday': [6, 13, 20, 27],
        'Saturday': [7, 14, 21, 28]
    }],
    ['December', 31, {
        'Sunday': [6, 13, 20, 27],
        'Monday': [7, 14, 21, 28],
        'Tuesday': [1, 8, 15, 22, 29],
        'Wednesday': [2, 9, 16, 23, 30],
        'Thursday': [3, 10, 17, 24, 31],
        'Friday': [4, 11, 18, 25],
        'Saturday': [5, 12, 19, 26]
    }]
]

if leapYear(currentYear):
    # changing the number of days from 28 to 29 (leap year)
    date[1][1] = 29

    updateDictionary(date[1][2], {
        'Sunday': [2, 9, 16, 23],
        'Monday': [3, 10, 17, 24],
        'Tuesday': [4, 11, 18, 25],
        'Wednesday': [5, 12, 19, 26],
        'Thursday': [6, 13, 20, 27],
        'Friday': [7, 14, 21, 28],
        'Saturday': [1, 8, 15, 22, 29],
    })
