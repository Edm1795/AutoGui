
def dayFinder(day,date):
    
   
    
    if day == 1:
        secondSunday=8
        
    else:
        secondSunday=8-(day-1)
        
    
    if date >= secondSunday:
        week = date//7 + 1
    else:
        week = 1
    
    return week
        
    
for num in range(1,31):
    print('Date:',num,dayFinder(6,num))

import datetime


def week(year, month, day):
    # Create a date object
    dateObj = datetime.date(year, month, day)

    # Get the ISO calendar week number and weekday
    isoYear, isoWeekNumber, isoWeekday = dateObj.isocalendar()

    # Calculate the week number within the month
    firstDayOfMonth = datetime.date(year, month, 1)
    firstWeekNumber = firstDayOfMonth.isocalendar()[1]
    weekNuminMon = isoWeekNumber - firstWeekNumber + 1

    return weekNuminMon

print(week(2023,12,12))
