import datetime

# cREAING Weekdays dictionaries
weekdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'

}
# Creating Months Dictionary

monthS = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: ' August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
d = datetime.datetime.today()
print(weekdays[d.weekday()])
print(monthS[d.month])
print(d.day)
print(d.strftime(" %I %M %p")) #prints AM and PM of Time