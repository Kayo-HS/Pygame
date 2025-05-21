import pygame 
# Importa a biblioteca Pygame para usar suas funcionalidades

from pygame.event import get 
#Importa a função get do módulo pygame.event para lidar com eventos como pressionar teclas ou clicar o mouse.

from pygame.locals import *
#Importa a função get do módulo pygame.event para lidar com eventos como pressionar teclas ou clicar o mouse.

from sys import exit 
#na quarta linha importo o botão de sair da janela para sair do programa


pygame.init()
#Inicializa todas as submódulos do Pygame, como a tela, o som e os gráficos.

larguraX = 640
alturaY = 480
#Define as dimensões da tela do jogo.


tela = pygame.display.set_mode((larguraX, alturaY))
# Cria uma tela com as dimensões especificadas.

pygame.display.set_caption("Berserk")
#define o nome do jogo


#Cria um loop infinito que mantém o jogo rodando até que o usuário decida sair.
while True:
    for event in pygame.event.get():
#Essa função é crucial para o seu jogo. Ela coleta todos os eventos que aconteceram desde a última vez que foi chamada, como:
#QUIT: O usuário clicou no botão "Fechar" da janela do jogo.
#KEYDOWN: Uma tecla foi pressionada.
#KEYUP: Uma tecla foi solta.
#MOUSEBUTTONDOWN: O mouse foi clicado.
#MOUSEBUTTONUP: O mouse foi solto.
#E muitos outros!
        if event.type == QUIT:
            pygame.quit()
            #Verifica se o evento é o usuário clicando no botão "Fechar". Se for, o jogo é fechado.
            exit()
    pygame.draw.rect(tela, (255,200,0), (200,300,40,50)) 
    pygame.draw.circle(tela,(0,0,255), (100,260), 40)
    pygame.draw.line(tela,(130,204,132), (390,0), (390,600), 50)
    

    #Explicando o Código

#pygame.draw.rect(tela, (255, 200, 0), (200, 300, 40, 50)):

#(tela: A superfície onde você está desenhando (a tela do jogo).
#(255, 200, 0): A cor do retângulo, usando valores RGB (vermelho, verde, azul). Neste caso, é um laranja.
#(200, 300, 40, 50): A posição e o tamanho do retângulo:
#(200, 300): A posição do canto superior esquerdo do retângulo na tela.
#40: A largura do retângulo.
#50: A altura do retângulo.
#pygame.draw.circle(tela, (0, 0, 255), (100, 260), 40):

#tela: A superfície onde você está desenhando.
#(0, 0, 255): A cor do círculo (azul).
#(100, 260): A posição do centro do círculo.
#40: O raio do círculo.
#pygame.draw.line(tela, (130, 204, 132), (390, 0), (390, 600), 50):

#tela: A superfície onde você está desenhando.
#(130, 204, 132): A cor da linha (verde).
#(390, 0): A posição do ponto inicial da linha.
#(390, 600): A posição do ponto final da linha.
#50: A espessura da linha.)#

    pygame.display.update() 
 #O pygame.display.update() faz exatamente isso para o seu jogo. Ele atualiza a tela para mostrar tudo que você desenhou, moveu ou alterou usando o Pygame.       


