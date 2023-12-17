import pyautogui as ag
import datetime


def clickDate():

    curDate=datetime.date.today() # get date object for current day; datetime.date.today() gives all three values ymd
    day=curDate.weekday() # extract the weekday from the current date object as an int 0-6 for Mon-Sat.

    def week(date=curDate.day, year=curDate.year, month=curDate.month):
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

    if week()==1:
        y = yDefault
    else:
        y = yDefault + (week() * yDiff)
    
    ag.moveTo(x,y)

clickDate()





# This one gives correct week in month but is not flexible for taking different days

import datetime
import calendar

def week(date=datetime.date.today().day, year=datetime.date.today().year, month=datetime.date.today().month):
    # Set Sunday as the first day of the week
    calendar.setfirstweekday(calendar.SUNDAY)

    # Create a date object
    dateObj = datetime.date(year, month, date)

    # Calculate the week number within the month where Sunday is the first day of the week
    first_day_of_month = datetime.date(year, month, 1)
    first_weekday = first_day_of_month.weekday()

    if first_weekday == 6:  # If the first day of the month is Sunday
        week_number_in_month = (date - 1) // 7 + 1
    else:
        first_sunday = 7 - first_weekday
        if date <= first_sunday:
            week_number_in_month = 1
        else:
            week_number_in_month = (date - first_sunday) // 7 + 2

    return week_number_in_month

# Test the function
week_number = week()
print("Week number in the month:", week_number)
