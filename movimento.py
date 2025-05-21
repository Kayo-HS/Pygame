import pygame
from pygame.locals import*
from sys import exit 

pygame.init()

largura = 640
altura = 480

x = largura/2 

y = 0

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Movimento")
relogio = pygame.time.Clock()

while True:
    relogio.tick(120)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    if y >= altura:
        y = 0
    y = y + 1
    


    pygame.display.update()

#((tela = pygame.display.set_mode((largura,altura)): Cria a tela do jogo com as dimensões definidas.
#pygame.display.set_caption("Movimento"): Define o título da janela do jogo como "Movimento".
#relogio = pygame.time.Clock(): Cria um objeto Clock para controlar a taxa de quadros (FPS) do jogo.
#Loop Principal:

#while True:: Cria um loop infinito que mantém o jogo rodando até que o jogador feche a janela.
#relogio.tick(120): Limita a taxa de quadros do jogo a 120 FPS. Isso significa que o código dentro do loop será executado no máximo 120 vezes por segundo.
#tela.fill((0,0,0)): Preenche a tela com a cor preta (RGB: 0, 0, 0) a cada frame, limpando a tela para o próximo desenho.
#for event in pygame.event.get():: Captura todos os eventos que ocorrem na janela do jogo, como pressionar teclas, clicar o mouse ou fechar a janela.
#if event.type == QUIT:: Verifica se o evento é do tipo QUIT (o jogador clicou no botão "X" para fechar a janela). Se sim, encerra o Pygame e o programa.
#pygame.draw.rect(tela, (255,0,0), (x,y,40,50)): Desenha um retângulo vermelho (RGB: 255, 0, 0) na tela. O retângulo tem 40 pixels de largura, 50 pixels de altura e está localizado na posição (x, y).
#if y >= altura:: Verifica se o retângulo chegou ao final da tela. Se sim, redefine a posição vertical y para 0, fazendo com que o retângulo "volte" para o topo da tela.
#y = y + 1: Move o retângulo para baixo em 1 pixel a cada frame.
#pygame.display.update(): Atualiza a tela, mostrando as alterações feitas.
#O que o código faz:

E#ste código cria um jogo simples em que um retângulo vermelho se move para baixo na tela. Quando o retângulo chega ao final da tela, ele "volta" para o topo. O loop while True mantém o jogo rodando até que o jogador feche a janela.

#Pontos importantes:

#A variável x define a posição horizontal do retângulo, que está fixo no centro da tela.
#A variável y define a posição vertical do retângulo, que é incrementada a cada frame, fazendo com que o retângulo se mova para baixo.
#O código usa pygame.display.update() para atualizar a tela após cada frame, mostrando as alterações feitas.))#    