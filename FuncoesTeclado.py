import pyautogui

'''Pressionar uma tecla'''
pyautogui.press("A tecla que quer ser pressionada")

'''Digitando caracteres'''
pyautogui.typewrite("Qual a sequencia de caracteres sera digitada")

'''Capaz de pressionar 2 ou mais teclas simultaneamente'''
pyautogui.hotkey("tecla1","tecla2","teclaN")

'''Pressiona uma tecla e mantem pressionada'''
pyautogui.keyDown("tecla")

'''Solta a tecla pressionada anteriormente'''
pyautogui.keyUp("tecla")

