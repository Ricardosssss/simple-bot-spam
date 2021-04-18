from time import sleep
import pyautogui

def infinito():
    x = (input('Mensagem: '))
    print('Vai começar em')
    for n in range(2, -1, -1):
        print(f'[ {n + 1} ]')
        sleep(1)
    
    while True:
        pyautogui.write(x)
        pyautogui.press('enter')

def contado():
        x = (input('Mensagem: '))
        q = int(input('Quantas vezes repetir? '))
        print('Vai começar em')
        for n in range(2, -1, -1):
            print(f'[ {n + 1} ]')
            sleep(1)
    
        for v in range(0, q):
            pyautogui.write(x)
            pyautogui.press('enter')
