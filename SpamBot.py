from time import sleep
import pyautogui

print('''
https://www.instagram.com/_.ricardosssss._/

 ,_._._._._._._._|________________________________________________________
 |_|_|_|_|_|_|_|_|_______________________________________________________/
                 !

 ███████╗██████╗  █████╗ ███╗   ███╗
 ██╔════╝██╔══██╗██╔══██╗████╗ ████║
 ███████╗██████╔╝███████║██╔████╔██║
 ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
 ███████║██║     ██║  ██║██║ ╚═╝ ██║
 ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
''')

print('''
[ 1 ]Spam infinito
[ 2 ]Spam contado
''')

e = int(input('Opção: '))

while 1:
    if e >= 3:
        print('''
[ 1 ]Spam infinito
[ 2 ]Spam contado
    ''')
        e = int(input('Opção: '))
    else:
        break

x = input('Mensagem: ')

if e == 1: 
    print('Vai começar em')
    for n in range(2, -1, -1):
        print(f'[ {n + 1} ]')
        sleep(1)
    
    while True:
        pyautogui.write(x)
        pyautogui.press('enter')

elif e == 2:
    q = int(input('Quantas vezes repetir? '))
    print('Vai começar em')
    for n in range(2, -1, -1):
        print(f'[ {n + 1} ]')
        sleep(1)
    
    for v in range(0, q):
        pyautogui.write(x)
        pyautogui.press('enter')
