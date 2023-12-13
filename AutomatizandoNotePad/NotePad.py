import pyautogui
import time
#Utilizar o sleep para causar um delay (neessario o time)

#Sequencia para abrir o notePad
pyautogui.hotkey("win","r")
pyautogui.write("notepad")
pyautogui.press("enter")


time.sleep(3)

#Inserir texto no notepad
'''Precionar o enter para permitir escrever'''
pyautogui.sleep(2)
pyautogui.press("enter")
pyautogui.typewrite("Hello World")
pyautogui.press("enter")
pyautogui.typewrite("Sejam bem vindos")
