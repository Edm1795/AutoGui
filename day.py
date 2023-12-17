import pyautogui as ag
import datetime


import datetime

def clickDate():
    curDate = datetime.date.today()  # get date object for current day; datetime.date.today() gives all three values ymd
    day = curDate.weekday()  # extract the weekday from the current date object as an int 0-6 for Mon-Sat.
    print('day', day,'today',curDate)

    def week(date=curDate.day, year=curDate.year, month=curDate.month):
        # Create a date object
        dateObj = datetime.date(year, month, date)

        # Calculate the week number within the month
        first_day_of_month = dateObj.replace(day=1)  # Get the first day of the month
        offset = (first_day_of_month.weekday() - 6) % 7  # Calculate the offset for Sunday as the first day of the week
        adjusted_date = first_day_of_month - datetime.timedelta(days=offset)  # Adjust the date to start on a Sunday
        week_number = (dateObj - adjusted_date).days // 7 + 1  # Calculate the week number
        print(week_number)
        return week_number

    return week()

# Example usage
print(clickD
