import pyautogui
import time

#pyautogui.sleep(2)
#print(pyautogui.position())
pyautogui.doubleClick(483,1079,duration=2)
pyautogui.sleep(2)
pyautogui.hotkey('ctrl','t')
pyautogui.sleep(2)
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
pyautogui.sleep(60)
pyautogui.click(294,212)
pyautogui.write('sunny')
pyautogui.sleep(1)
pyautogui.press('enter')
pyautogui.sleep(2)
pyautogui.write('''Automating whatsapp...
It's a testing protocol''')
pyautogui.press('enter')