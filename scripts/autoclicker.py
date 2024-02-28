# Autoclicker of 100 clicks in 30 seconds

import pyautogui

#  ======== settings ========
delay = .3  # in seconds
#  ==========================

def displaySettings():
    print("// Time to complete -> 30s")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    

def displayComplete():
    print("Task Complete -> 100 clicks done")

def main():

    displaySettings()
    i = 0
    while i < 100:
        pyautogui.click()
        pyautogui.PAUSE = delay
        i = i + 1

    displayComplete()

main()
