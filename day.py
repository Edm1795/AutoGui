
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
