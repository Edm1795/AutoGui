import pyautogui as ag

def clickDate(day):

    yDiff = 32 # number of pixels between adjacent rows (eg week 1 - week 2)
    xDiff = 36 # number of pixels between immediately adjacent days of week (eg:mon-tues)
    xDefault = 851 # 36 pixel difference
    yDefault = 301

    if day == 1:
        x= xDefault
    elif day == 2:
        x = xDefault + (xDiff)
    else:
        x = xDefault + (day*xDiff)

    
    y = 301
    
    ag.moveTo(x,y)

clickDate(3)
        
