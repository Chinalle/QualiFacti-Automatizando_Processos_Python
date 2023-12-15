'''declarar as bibliotecas necessarias'''
import pyautogui
import time
import cv2

'''define um tempo de pausa e um mode de falha segura'''
pyautogui.PAUSE = 3
pyautogui.FAILSAFE = True


'''Abrir o formulario no navegador padrão'''
pyautogui.hotkey("win","r")
pyautogui.typewrite("https://forms.gle/otsFeQsiKjmhdnqC8 \n")


'''Esperar 5 segundos para que a pagina carregue'''
time.sleep(5)


'''Abrir o arquivo CSV contendo os dados dos membros da biblioteca'''
# "as f" vai quebrar a planilha em linhas para organizar  
with open("membros_biblioteca.csv") as f:
    #tirando o cabeçalho da planilha, pulando a primeira linha do arquivo
    next(f)

    #Para cada linha do arquivo CSV 
    for line in f:
        #extrair os dados dos membros: Nome, email e telefone
        line = line.strip() #remove espaçoes não preenchidos (branco)
        line = line.split(";") #divide a linha em uma lista  separados por ;
        
        #imprimir os dados dos membros 
        print("Dados: ", line)

        #atribuir as informações da lista para a variavel
        name = line[0]
        email = line[1]
        phone = line[2]
        print(name, email, phone)

        #Localizar a imagem do campo "Nome do funcionario na tela
        pyautogui.locateCenterOnScreen("nome.png",confidence=0.8) #confidence é a confiança do reconhecimento da imagem (de 0 a 1)
        pyautogui.click(pyautogui.locateCenterOnScreen("resposta.png",confidence=0.8),duration=1)
        pyautogui.typewrite(name, interval=0.25) #interval é o intervalo da escrita entre uma letra e outra

        pyautogui.locateCenterOnScreen("email.png",confidence=0.8) 
        pyautogui.click(pyautogui.locateCenterOnScreen("resposta.png",confidence=0.8),duration=1)
        pyautogui.typewrite(email, interval=0.25)


        pyautogui.locateCenterOnScreen("telefone.png",confidence=0.8) 
        pyautogui.click(pyautogui.locateCenterOnScreen("resposta.png",confidence=0.8),duration=1)
        pyautogui.typewrite(phone, interval=0.25)

        #Tira uma captura 
        pyautogui.screenshot(f"cadastro_{name}.png")

        #Enviar os dados preenchidos
        pyautogui.click(pyautogui.locateCenterOnScreen("enviar.png",confidence=0.8))

        #Espera 3 segundos para que possa selecinar a opção nova resposta
        time.sleep(3)
        #Clicar no botão "Outro cadastro"
        pyautogui.click(pyautogui.locateCenterOnScreen("outrocadastro.png",confidence=0.8))

        #Exibi uma imagem de alerta informando que o programa foi finalizado com sucesso 
        
      