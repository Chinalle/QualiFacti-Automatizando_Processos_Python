import pyautogui
import time

for i in range(4):
    #Tira o screenshoot e da um nome para ele -> "print + hora do print + .png"
    pyautogui.screenshot(f"print_{time.time()}.png")
    time.sleep(2)