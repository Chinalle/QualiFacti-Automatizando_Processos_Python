import pyautogui

'''Para o usuario posicionar o mouse onde quer'''
pyautogui.PAUSE = 0.5

# Sequencia para que o paint seja iniciado
'''Automação do teclado'''

'''Preciona duas teclas ao mesmo tempo'''
pyautogui.hotkey("win","r")

'''Digitando'''
pyautogui.write("mspaint")

'''Preciosando uma tecla'''
pyautogui.press("enter")

'''Mover o mouse para a posição do lapis'''
x,y = (310,101) #Sera necessário ajuste de coordenada
pyautogui.click(x,y)


pyautogui.moveTo(260,265) #Sera necessário ajuste de coordenada

pyautogui.PAUSE = 2.5   

#pyautogui.displayMousePosition()

distance = 400
while distance >0:
    #Arrasta um iten, o lapis
    pyautogui.dragRel(distance, 0, duration=0.5)
    #Degremento para que não fique uma linha em cima da outra
    distance -= 25
    pyautogui.dragRel(0,distance,duration=0.5)
    pyautogui.dragRel(-distance,0,duration=0.5)
    distance -= 25
    pyautogui.dragRel(0,-distance,duration=0.5)

