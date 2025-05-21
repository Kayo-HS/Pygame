import pygame
from pygame.locals import*
from sys import exit 
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.4)
musicaFundo = pygame.mixer.music.load("never meant to belong.mp3")
pygame.mixer.music.play(-1)

barulhoColissao = pygame.mixer.Sound("collect-points-190037.mp3")
barulhoColissao.set_volume(.2)

largura = 640
altura = 480
x = int(largura/2)
y = int(altura/2)

xAzul = randint(40, 600)
yAzul = randint(50, 400)

fonte = pygame.font.SysFont("Arial", 40, True, True)
pontos = 0 

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game")

relogio = pygame.time.Clock()

while True:

    relogio.tick(120)
    tela.fill((0,0,0))
    mensagem = (f"PONTOS: {pontos}")
    textoFormado = fonte.render(mensagem,False, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_LEFT]:
        x = x - 10
        if x < 0:
            x = 0
    if pygame.key.get_pressed()[K_RIGHT]:
        x = x + 10
        if x > largura - 40:
            x = largura - 40
    if pygame.key.get_pressed()[K_DOWN]:
        y = y + 10
        if y > altura - 50:
            y = altura - 50
    if pygame.key.get_pressed()[K_UP]:
        y = y - 10
        if y < 0:
            y = 0
    
    retVermelho = pygame.draw.rect(tela, (255,0,0), (x, y, 40, 50))
    retAzul = pygame.draw.rect(tela, (0,0,255), (xAzul, yAzul, 70, 80))

    if retVermelho.colliderect(retAzul):
        xAzul = randint(100, 500)
        yAzul = randint(100,400)
        pontos = pontos + 1
        barulhoColissao.play()

    tela.blit(textoFormado, (400, 40))
    pygame.display.update()
    