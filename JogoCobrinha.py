import pygame
from pygame.locals import*
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.3)
musicaFundo = pygame.mixer.music.load("never meant to belong.mp3")
pygame.mixer.music.play(-1)


barulhoColissao = pygame.mixer.Sound("collect-points-190037.mp3")
barulhoColissao.set_volume(0.2)


largura = 640
altura = 480
xCobra = int(largura/2)
yCobra = int(altura/2)

xMaca = randint(40, 600)
yMaca = randint(50, 400)

fonte = pygame.font.SysFont("Arial", 40, True, True)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Som")
relogio = pygame.time.Clock()

listaCobra = []

def aumentaCobra(listaCobra):
    for XeY in listaCobra:
        pygame.draw.rect(tela,(0,255,0), (XeY[0], XeY[1], 20,20))

while True:

    relogio.tick(120)
    tela.fill((255,255,255))
    mensagem = (f"PONTOS: {pontos}")
    textoFormado = fonte.render(mensagem,False, (0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_a]:
        xCobra = xCobra - 10
        if xCobra < 0:
            xCobra = 0

    if pygame.key.get_pressed()[K_d]:
        xCobra = xCobra + 10
        if xCobra > largura - 40:
            xCobra = largura - 40

    if pygame.key.get_pressed()[K_s]:
        yCobra = yCobra + 10
        if yCobra > altura - 50:
            yCobra = altura - 50

    if pygame.key.get_pressed()[K_w]:
        yCobra = yCobra - 10
        if yCobra < 0:
            yCobra = 0     

    Cobra = pygame.draw.rect(tela, (0,255,0), (xCobra, yCobra, 20, 20))
    
    Maca = pygame.draw.rect(tela, (255,0,0), (xMaca, yMaca, 20, 20))

    if Cobra.colliderect(Maca):
        xMaca = randint(100, 500)
        yMaca = randint(100, 400)
        pontos = pontos + 1
        barulhoColissao.play()
        listaCabeça = []
        listaCabeça.append(xCobra)
        listaCabeça.append(yCobra) 
        listaCobra.append(listaCabeça)
    
    aumentaCobra(listaCobra)


    tela.blit(textoFormado,(400, 40))
    pygame.display.update()
