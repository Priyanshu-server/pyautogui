#scrolling #holding

import pyautogui,time

time.sleep(2)
'''
pyautogui.mouseDown(302,456);
time.sleep(2)
pyautogui.mouseUp()
'''

for i in range(100):

    pyautogui.scroll(-500)
    time.sleep(1)