import pyautogui as pg
import time
import pyperclip
import os

x = int(input("Digite um número: "))
# Pega o número a ser usado como fatorial

print("Agora, se afaste do mouse e teclado....")
os.system("start calc.exe")
# Abre a calculadora
# Nota: a minha automaticamente é a científica, e isso fará diferença mais pra frente
time.sleep(10)
# tempinho pro pc da xuxa abrir a calculadora
for i in range(1, x+1):
# Itera os valores de 1 até o número do fatorial
# Ex.: 4! = 1 * 2 * 3 * 4
    for index, num in enumerate(str(i)):
    # Enumera a quantidade de dígitos por número, irrelevante para números abaixo de 10
        if str(i)[index-1] == num and index > 0:
        # Se o dígito atual for igual ao anterior, a calculadora tem um pequeno problema
        # de mudança de cor ao redor do número pressionado por algum motivo
        # Então pra números repetidos (ex 11, 22, 111), tenho que clicar em outro ponto da tela antes
            reset = pg.locateCenterOnScreen('teclas/cientifica.png')
            pg.click(reset.x, reset.y, duration=0.5)
        numeroPath = 'teclas/' + num + '.png'
        # Pega o caminho ja definido da tecla atual
        tecla = pg.locateCenterOnScreen(numeroPath)
        pg.click(tecla.x, tecla.y, duration=0.125)

    mult = pg.locateCenterOnScreen('teclas/x.png')
    pg.click(mult.x, mult.y, duration=0.125)
    # Clica pra multiplicar

pg.moveTo(pg.locateCenterOnScreen("teclas/historico.png"))
pg.move(0, 75)
# Como o resultado varia com o número escolhido, tomamos como principio o botao de historico
# que fica logo acima do resultado, independente da posição da calculadora na tela
# e então deslocamos o mouse até o resultado de fato
resultNum = pg.position()
pg.doubleClick()
pg.rightClick()
pg.move(0, -50, 0.5)

selec = pg.locateCenterOnScreen("teclas/selecionar.png")
pg.click(selec.x, selec.y)
pg.move(0, -50, 0.5)
# Seleciona o resultado

pg.moveTo(resultNum)
pg.rightClick()
pg.move(0, -50, 0.5)
copiar = pg.locateCenterOnScreen("teclas/copiar.png")
pg.doubleClick(copiar.x, copiar.y, duration=0.5)
time.sleep(1)
# Copia o resultado

# Temos que deslocar o mouse um pouco pra cima nesses menus de clique direito
# pois sua presença atrapalha a detecção dos botões (?)

print("R: ", pyperclip.paste())
# Exibe o resultado