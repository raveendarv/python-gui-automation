import subprocess
import pyautogui
import time

with open('code.txt', 'r') as f:
    contents = f.read()

subprocess.Popen([r"C:\Users\ravin\AppData\Local\Postman\Postman.exe"])
time.sleep(11)

pyautogui.click(x=962, y=294)
pyautogui.hotkey('ctrl', 'a')
pyautogui.typewrite(contents)


# pyautogui.displayMousePosition()
# print(pyautogui.position()) Use it to get the position of the cursor

# while(1):
#     if (pyautogui.locateCenterOnScreen('Screen.png')):
#         break
# print(pyautogui.locateCenterOnScreen('Screen.png'))