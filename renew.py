from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#from selenium.webdriver.common.action_chains import ActionChains
# note one day of due date code says: '<span>Due today</span>'
x = '21221'
y = '9'

print('    opening browser')
br = webdriver.Firefox()
br.get('https://epl.bibliocommons.com/user/login?destination=https%3A%2F%2Fwww.epl.ca%2F&_ga=2.262750156.1531422150.1564462487-629941795.1536456122')

seaname = br.find_element_by_name('name') # find fields on page
seapin = br.find_element_by_name('user_pin')
print('    logging into website')

seaname.send_keys(x) # send in credentials
seapin.send_keys(y)

seapin.send_keys(Keys.RETURN) # hit return to log in

time.sleep(3)

print('    navigating to checkouts')
br.get('https://epl.bibliocommons.com/v2/checkedout/out') # skip over to checkedout items page
time.sleep(2)

renewbtn = br.find_elements_by_xpath("//button[@class='cp-btn btn cp-primary-btn btn-primary cp-renew-button btn-block']")
# select box for each book
selctbox = br.find_elements_by_xpath("//button[@class='check hide-icon']")# "clear" button which pops up after each click on select box

# find due date countdown, then pull out text (ex: "12 days remaining")
duedates = br.find_elements_by_xpath("//span[@class='due-date-notice']")

time.sleep(5)
# find and click button listing all items in case not already showing by default
try:
    allitems = br.find_element_by_xpath("//a[@class='cp-sidebar-link cp-status-sidebar-link cp-all-sidebar-link all']")
    print('    click allitems button')
    allitems.click()
#cp-sidebar-link cp-status-sidebar-link cp-all-sidebar-link all
#duedatenum = duedates[:2]
except:

    print('   checking for items nearly due')
    c = 0
    for i in duedates :
        time.sleep(1)
        c = c + 1
        num = i.text
        num = num[:2]
        num = int(num)
        print('     ',num,'days remaining on item')
        if num < 4 :
            renewbtn[c].click()
        # scroll to position of next renewbtn
            br.execute_script('arguments[0].scrollIntoView(true);', selctbox[c+1])
    #else : print('    no items nearly due')


# note, elements will make a list of all
#renewbtn[0].click -- select the button from the list you want to click
# make a list of all renew buttons

#count = -1
#or btn in renewbtn :  # loop through list of buttons and click them
#    count = count + 1
#    renewbtn[count].click()
#    time.sleep(2)
#        renewbtn[count].click()

# "clear" button which pops up after each click on select box

#for btn in renewbtns :  # loop through list of buttons and click them
#    count = count + 1
#    for duedate in duedates
#        dnum = duedate[:2]
#        while dnum < 4  :
#            renewbtn[count].click
#            else continue

#clrbtn = br.find_element_by_xpath("//button[@class='cp-btn btn cp-text-btn clear-button']")
#actions = ActionChains(br)
