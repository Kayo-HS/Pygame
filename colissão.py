import pygame
from pygame.locals import* 
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2

xAzul = randint(70,620)
yAzul = randint(60,450)


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Colissão")
relogio = pygame.time.Clock()

while True:
    relogio.tick(120)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_a]:
        x = x - 10
    if pygame.key.get_pressed()[K_d]:
        x = x + 10            
    if pygame.key.get_pressed()[K_s]:
        y = y + 10    
    if pygame.key.get_pressed()[K_w]:
        y = y - 10
    retVermelho = pygame.draw.rect(tela,(255,0,0),(x,y,40,50))
    retAzul = pygame.draw.rect(tela,(0,0,255),(xAzul,yAzul,50,60))

    if retVermelho.colliderect(retAzul):
        xAzul = randint(70,620)
        yAzul = randint(60,450)
        

    pygame.display.update()        