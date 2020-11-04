import pyautogui,time

# pyautogui.screenshot("snap1.jpg")

# im = pyautogui.screenshot(region=(0,0,300,400))
# im.show()
'''
taskClick = pyautogui.locateOnScreen("task.png",confidence = 0.7) #defualt confidence level = 0.9
print(taskClick)
'''
# print(list(pyautogui.locateAllOnScreen('task.png',confidence = 0.7)))

x = pyautogui.locateCenterOnScreen("task.png",confidence = 0.8,region  = (0,820,1409,1079))
pyautogui.moveTo(x)