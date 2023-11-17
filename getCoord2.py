import pyautogui as ag


looping=True
while looping:

    input('place mouse then type d')

    print(ag.position())

    ans=input('to go again type c')

    if ans!='c':
        looping=False

print('complete')
