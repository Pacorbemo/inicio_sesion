import pyautogui as pa 
from time import sleep

#Abrir chrome
pa.press('win')
sleep(1)
pa.write('chrome', 0.05)
pa.press('enter')
sleep(2)
pa.hotkey('ctrl','shift', 'n')
sleep(1)
pa.hotkey('win','up')

def direccion(nombre):                                      #Ejemplo ('gmail')
    pa.write(nombre, 0.05)
    pa.press('enter')
    sleep(3)

def autenticar(nombre,dominio,direccion_contraseña):        #Ejemplo (Paco, gmail, C:\\Users\Documents\contraseña.txt)
    pa.write(nombre) 
    pa.hotkey('altright', '2')
    pa.write(dominio)
    sleep(0.5)
    pa.press('enter')
    f = open(direccion_contraseña, "r")
    sleep(2)
    pa.write(f.read())
    pa.press('enter')

def autenticar_sin_contraseña(nombre,dominio):                #Ejemplo (Paco,gmail)
    pa.write(nombre) 
    pa.hotkey('altright', '2')
    pa.write(dominio)
    sleep(0.5)
    pa.press('enter')
