from datetime import datetime


import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print('localtime',current_time)

now = datetime.now()
currTime=now.strftime("%H:%M:%S")

start = datetime.strptime("8:00:00", "%H:%M:%S") 
end = datetime.strptime(currTime, "%H:%M:%S") 

difference = end - start 

seconds = difference.total_seconds() 
print('difference in seconds is:', seconds) 

minutes = seconds / 60
print('difference in minutes is:', minutes) 

hours = seconds / (60 * 60) 
print('difference in hours is:', hours)

print('gmtime',time.gmtime())

print(currTime)

print('now time',now.time())

ctime1 = time.ctime()
print(ctime1)
