


rawSched='''EPL,Schedule Report,,,,,,Dayforce HCM
"Riverbend Branch Site
Date Range:  1/07/2024 - 1/13/2024
Week numbers:  1, 2
Department: Riverbend BranchJob: Library AssistantActivity: CS, IN, MTG, OTF",,,,,,,"Run Date:  1/11/2024 1:35:35 PM
Run By:  VIRCLE"
EPL,,,,,,,
Employee,"Sun, 01/07","Mon, 01/08","Tue, 01/09","Wed, 01/10","Thu, 01/11","Fri, 01/12","Sat, 01/13"
Anna-Maria Barczak,"Library Assistant
9:10 AM - 5:10 PM
CS: 10:00 AM - 11:00 AM
CS: 11:30 AM - 12:30 PM
OTF: 1:30 PM - 2:00 PM
CS: 3:00 PM - 4:00 PM
CS: 4:30 PM - 5:10 PM",ÿ,"Library Assistant
9:00 AM - 6:00 PM
CS: 1:00 PM - 2:00 PM
CS: 3:00 PM - 3:30 PM
OTF: 4:00 PM - 4:30 PM
CS: 4:30 PM - 5:10 PM","Library Assistant
1:10 PM - 9:10 PM
CS: 1:10 PM - 2:00 PM
OTF: 4:00 PM - 4:30 PM
CS: 6:00 PM - 7:00 PM
CS: 8:00 PM - 9:10 PM","Library Assistant
9:00 AM - 6:00 PM
CS: 11:00 AM - 12:00 PM
CS: 4:00 PM - 5:30 PM",Earned Day Off,ÿ
Carole Rykes,ÿ,"Library Assistant
2:00 PM - 6:00 PM
CS: 2:00 PM - 3:00 PM
CS: 5:00 PM - 6:00 PM",VAC Taken 12:00 PM - 4:00 PM,VAC Taken 12:00 PM - 4:00 PM,"Library Assistant
5:10 PM - 9:10 PM
CS: 5:30 PM - 6:00 PM
CS: 8:30 PM - 9:10 PM",ÿ,VAC Taken 12:00 PM - 4:00 PM
Laura Young,ÿ,"Librarian (Community)
9:00 AM - 5:00 PM",ÿ,ÿ,ÿ,"Librarian (Community)
9:00 AM - 5:00 PM
MTG: 10:00 AM - 11:30 AM
MTG: 11:30 AM - 12:30 PM
MTG: 4:00 PM - 4:30 PM",ÿ
Donna Leslie,ÿ,Earned Day Off,"Page
8:30 AM - 5:00 PM
IN: 9:00 AM - 10:00 AM
IN: 4:00 PM - 5:00 PM","Page
8:00 AM - 4:30 PM
IN: 1:00 PM - 2:00 PM","Page
8:00 AM - 4:30 PM
IN: 8:30 AM - 9:00 AM
IN: 1:00 PM - 2:00 PM",ÿ,"Page
8:30 AM - 5:00 PM
IN: 9:00 AM - 10:00 AM
IN: 2:30 PM - 3:00 PM
IN: 4:00 PM - 5:00 PM"
'''

schedList=rawSched.split() # split at spaces
schedList2=rawSched.splitlines() # split at new lines -- This one looks better

csList=[]

for item in schedList2:

    if item[0]=='C':
        csList.append(item)


print(schedList2)

print(csList)
