import pyautogui, time
time.sleep(2)
distance =200

while distance>0:
    pyautogui.drag(distance,0,duration=0.15)
    distance -= 5
    pyautogui.drag(0,distance,duration=0.15)
    pyautogui.drag(-distance,0,duration=0.15)
    distance -=5
    pyautogui.drag(0,-distance,duration=0.15)


