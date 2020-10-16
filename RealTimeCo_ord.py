import pyautogui

while True:
    x,y = pyautogui.position()
    string = 'X:' + str(x).rjust(4) + " Y:" + str(y).rjust(4)
    print(string,end="")
    print('\b'*len(string),end = '')

