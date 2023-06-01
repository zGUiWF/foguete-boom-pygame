import pygame
import random

def renderizarTexto(texto, tamanho, x, y, cor):
    fonte = pygame.font.Font(None, tamanho)
    texto_renderizado = fonte.render(texto, True, cor)
    tela.blit(texto_renderizado, (x, y))

pygame.init()

#nome do jogo
pygame.display.set_caption("Foguete Bumm!")

#icone do jogo
icone = pygame.image.load("icone.ico")
pygame.display.set_icon(icone)

#tela
tamanho = (600, 600)
tela = pygame.display.set_mode(tamanho)

#cores
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)

#fps
fps = 120

#imagens
nave = pygame.image.load("nave.png")
backgroud = pygame.image.load("backgroud.png")
missil = pygame.image.load("missil.png")

#foguete
fogueteX = 300
foguetemovimentoX = 0

#missil
posicaoMissil = 300
movimentoMissil = -50
velocidademissil = 1

#pontos iniciais
pontos = 0

#pixels a iguinorar na colisão
dificuldade = 70

#efeitos sonoros
meteoroSound = pygame.mixer.Sound("meteoro.mp3")
pygame.mixer.music.load("trilha.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.Sound.play(meteoroSound)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                foguetemovimentoX = 5
            elif event.key == pygame.K_LEFT:
                foguetemovimentoX = -5

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            foguetemovimentoX = 0
        elif event.key == pygame.K_LEFT:
            foguetemovimentoX = 0
          
    if fogueteX < 25 :
        fogueteX = 25
    elif fogueteX>575:
        fogueteX = 575
    else:
        fogueteX = fogueteX + foguetemovimentoX
    
    tela.blit(backgroud,(0,0))

    if movimentoMissil >= 600:
        movimentoMissil = -100
        posicaoMissil = random.randint(10,590)
        pontos = pontos + 1
        velocidademissil = velocidademissil + 1
        pygame.mixer.Sound.play(meteoroSound)


    movimentoMissil = movimentoMissil + velocidademissil
    renderizarTexto((f'Pontos: {pontos}'),35,10,10,branco)
    tela.blit(missil,(posicaoMissil,movimentoMissil))
    tela.blit(nave, (fogueteX-25,450))

    #colisão
    pixelsYnave = list(range(450,550))
    pixelsXnave = list(range(fogueteX, fogueteX + 100))

    pixelsYMeteoro = list(range(movimentoMissil, movimentoMissil+100)) #101 é o tamanho da imagem
    pixelsXMeteoro = list(range(posicaoMissil, posicaoMissil+100))

    if len(list(set(pixelsXnave) & set(pixelsXMeteoro))) > dificuldade:
        if len(list(set(pixelsYnave) & set(pixelsYMeteoro))) > dificuldade:
            tela.fill(preto)
            renderizarTexto('GAME OVER!',100,70,240,vermelho)
            renderizarTexto(f'Pontos: {pontos}',35,225,320,branco)
            pygame.display.flip()
            pygame.time.wait(5000)
            running = False
            
    pygame.display.update()
    pygame.time.Clock().tick(fps)
pygame.quit()

