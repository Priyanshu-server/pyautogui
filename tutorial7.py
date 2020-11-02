import pyautogui,time

#alert
time.sleep(1)
'''
alert = pyautogui.alert(text="This is alert for hacking ",title="ALERT",button="OK")
print(alert)
'''
#confirm()
'''
confirm = pyautogui.confirm(text="This is some confirmation",title = "Confirm",buttons=['OK','cancel'])
print(confirm)
'''
#prompt
'''
prompt = pyautogui.prompt(text="Input Something",title="Valid inputs",default=" ")
print(prompt)
'''
#password
password = pyautogui.password(text="passcode",title="carefully",default="",mask=":")
print(password)