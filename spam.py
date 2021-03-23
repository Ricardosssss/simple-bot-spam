import time
import pyautogui

mensagem = input('Mensagem de spam: ')

time.sleep(5)

while 1:
    pyautogui.typewrite(mensagem)
    pyautogui.press('enter')


