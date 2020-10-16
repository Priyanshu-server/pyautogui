import pyautogui
import time

size_x,size_y = pyautogui.size()
print(size_x,size_y)

# time.sleep(2) #pause the program for 2 sec

# position_x,position_y = pyautogui.position()
# print(position_x,position_y)

print(pyautogui.onScreen(1919,10))