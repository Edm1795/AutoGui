import pyautogui as ag
import datetime


def clickDate(day):

    def week(date, year=2024, month=12):
        # Create a date object
        dateObj = datetime.date(year, month, date)

        # Get the ISO calendar week number and weekday
        isoYear, isoWeekNumber, isoWeekday = dateObj.isocalendar()

        # Calculate the week number within the month
        firstDayOfMonth = datetime.date(year, month, 1)
        firstWeekNumber = firstDayOfMonth.isocalendar()[1]
        weekNuminMon = isoWeekNumber - firstWeekNumber + 1

        print(weekNuminMon)
        return weekNuminMon

    yDiff = 32 # number of pixels between adjacent rows (eg week 1 - week 2)
    xDiff = 36 # number of pixels between immediately adjacent days of week (eg:mon-tues)
    xDefault = 851 # 36 pixel difference
    yDefault = 301

    if day == 1:
        x= xDefault
    elif day == 2:
        x = xDefault + (xDiff)
    else:
        x = xDefault + ((day-1)*xDiff)

    if week(1)==1:
        y = yDefault 
    else:
        y = yDefault + (week(1) * yDiff)
    
    ag.moveTo(x,y)

clickDate(6)
