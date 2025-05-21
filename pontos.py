import pygame
from pygame.locals import*
from sys import exit 
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura/2
y = largura/2

xAzul = randint(40, 600)
yAzul = randint(50,530)

fonte = pygame.font.SysFont('Arial', 40, True, True)
pontos = 0

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Pontos")
relogio = pygame.time.Clock()

while True:

    relogio.tick(120)
    tela.fill((0,0,0))
    mensagem = (F"PONTOS: {pontos}")
    textoFormatado = fonte.render(mensagem,False, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20    

    retVermelho = pygame.draw.rect(tela,(255,0,0), (x,y,40,50))

    retAzul = pygame.draw.rect(tela,(0,0,255), (xAzul,yAzul,70,80))

    if retVermelho.colliderect(retAzul):
        xAzul = randint(100, 500)
        yAzul = randint(100,500)
        pontos = pontos + 1
    tela.blit(textoFormatado,(400,40))
    pygame.display.update()    
