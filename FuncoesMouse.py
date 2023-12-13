import pyautogui

#funções de automação do mouse

'''Move o cursor do mouse para uma posição especifica na tela,
de acordo com as coordenadas (x,y). O comando duration é o tempo,
nesse caso em segundos, que ele deve se mover'''
pyautogui.moveTo(x,y, duration=seconds)

'''Move o cursor do mouse em relação a posição atual, deslocando pelos valores de x e y'''
pyautogui.move(xOffset, yOffset, duration=seconds)

'''Click no mouse na posição especificada. O parametro click é
a quantidade de clicks e o intervalo é o intervalo entre um 
click e outro. Button é se vai ser feito o click com o 
direito ou esquerdo'''
pyautogui.click(x=None, y=None, click = 1, interval = 0.0, button = 'left')


'''A diferença é que é realizado dois clicks.'''
pyautogui.doubleClick(x=None, y=None, interval = 0.0, button = 'left')

'''Realiza o click com o botão direito nas coordenadas especificadas'''
pyautogui.rightClick(x=None, y=None, click = 1, interval = 0.0, button = 'left')

'''Realiza o click com o botão esquerdo nas coordenadas especificadas'''
pyautogui.leftClickClick(x=None, y=None, click = 1, interval = 0.0, button = 'left')

'''Scroll do mouse (rolagem)'''
pyautogui.scroll(clicks, x=None, y=None)

'''Arrasta o mouse de onde ele esta ate a coordenada passada'''
pyautogui.dragTo(x,y,duration=seconds)
'''Arrasta para as coordenadas solicitadas'''
pyautogui.drag(x,y,duration=seconds)

'''Retorna as coordenadas atuais do cursor na tela'''
pyautogui.position()

'''Retorna o tamanho (resolução) da tela'''
pyautogui.size()

'''Mostra em tempo real as coordenadas x e y do cursor'''
pyautogui.displayMousePosition()

'''Gera um delay de 2.5 segundos a cada ação do mouse'''
pyautogui.PAUSE = 2.5

