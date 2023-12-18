import pyautogui
import time
import cv2

pyautogui.PAUSE = 3
pyautogui.FAILSAFE = True


pyautogui.hotkey("win","r")
pyautogui.typewrite("https://forms.gle/C7SR5eeFUBjJ6KLA6 \n")


time.sleep(5)


with open("Alunos.csv") as f:
    next(f)

    for line in f:
        line = line.strip() 
        line = line.split(";") 
        
        print("Dados: ", line)

        name = line[0]
        ra = line[1]
        dataNascimento = line[2]
        print(name, ra, dataNascimento)

        
        pyautogui.locateCenterOnScreen("nomeAluno.png",confidence=0.8) 
        pyautogui.click(pyautogui.locateCenterOnScreen("resposta.png",confidence=0.8),duration=1)
        pyautogui.typewrite(name, interval=0.25) 

        pyautogui.hotkey("tab")
        pyautogui.typewrite(ra, interval=0.25)

        pyautogui.hotkey("tab")
        pyautogui.typewrite(dataNascimento, interval=0.25)

        pyautogui.screenshot(f"cadastro_{name}.png")

        pyautogui.click(pyautogui.locateCenterOnScreen("enviar.png",confidence=0.8))

        time.sleep(3)
        
        pyautogui.click(pyautogui.locateCenterOnScreen("outraResposta.png",confidence=0.8))

    
        
      