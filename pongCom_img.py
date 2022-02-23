import pygame
import random

pygame.init()
largura = 880
altura = 500

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Pong tipo o classico')
# player
posicao_player = 200
movimento = 0
playerx = 17
# bola
bolaX = largura/2
bolaY = 240
bola_movX = random.choice((-7, 7))
bola_movY = random.choice((-4, 4))
# oponente
oponentX = 850
oponentY = 200
movimentoOp = 0
run = True
# pontos
pontos = 0


# pontos do oponente
pontosOp = 0
fonteOp = pygame.font.Font(None, 50)
textoOp = fonteOp.render(f'{pontosOp}', True, (255, 255, 255))
# sons
# musica = pygame.mixer.music.load('BoxCat Games - Battle (Normal).mp3')
# pygame.mixer.music.play(-1)
colisao = pygame.mixer.Sound('somaobater.wav')
colisao_player = pygame.mixer.Sound('impacto.wav')
saida = pygame.mixer.Sound('impacto2.wav')
esplosao = pygame.mixer.Sound('explosion1.wav')
# imagens
#bolaJ = pygame.image.load('cranio.png')
#bolaJo = pygame.transform.scale(bolaJ, (64, 64))

# player
player1 = pygame.image.load('oso.png')
player1j = pygame.transform.scale(player1, (150, 100))

# combo do player

combo_player = 0
combo_Op = 0
certificado = 0
certificado_Op = 0
definition_combo = 1
while run:

    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            # movimento player
            if event.key == pygame.K_w:
                movimento = -10
            if event.key == pygame.K_s:
                movimento = 10
            # movimento oponente
            if event.key == pygame.K_UP:
                movimentoOp = -10
            if event.key == pygame.K_DOWN:
                movimentoOp = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                movimento = 0
            if event.key == pygame.K_s:
                movimento = 0

            if event.key == pygame.K_UP:
                movimentoOp = 0
            if event.key == pygame.K_DOWN:
                movimentoOp = 0

    posicao_player += movimento
    oponentY += movimentoOp

    if combo_player == 10 and certificado == 10:
        if boll.colliderect(player):
            bola_movX = 50
            bola_movY = random.choice((24, -24))
            esplosao.play()
            combo_player = 0

    if combo_Op == 10 and certificado_Op == 10:
        if boll.colliderect(oponent):
            bola_movX = -50
            bola_movY = random.choice((24, -24))
            esplosao.play()
            combo_Op = 0

    # bola movimento
    bolaX += bola_movX
    bolaY += bola_movY

    # barreira bola com o chao
    if bolaY > 480:
        bola_movY = -9
        colisao.play()
    if bolaY <= 0:
        bola_movY = 9
        colisao.play()
    # se a bola sair da tela
    fonte = pygame.font.Font(None, 50)
    texto = fonte.render(f'{pontos}', True, (255, 255, 255))
    fonteOp = pygame.font.Font(None, 50)
    textoOp = fonteOp.render(f'{pontosOp}', True, (255, 255, 255))

    # textos combos
    combo_fonte = pygame.font.Font(None, 48)
    combo_jogador = combo_fonte.render(
        f'Combo: {combo_player}', True, (255, 255, 255))

    # combo do oponente
    combo_enemy = combo_fonte.render(
        f'Combo: {combo_Op}', True, (255, 255, 255))

    if bolaX > largura:
        bolaX = largura/2
        bolaY = random.randint(100, 400)
        bola_movY = random.choice((1, -1))
        bola_movX = random.choice((5, -5))
        pontos += 1
        saida.play()
        combo_Op = 0
        #combo_player += 1
        certificado_Op = 0
    if bolaX < -10:
        bolaX = largura/2
        bolaY = random.randint(100, 400)
        bola_movY = random.choice((1, -1))
        bola_movX = random.choice((5, -5))
        pontosOp += 1
        saida.play()
        #combo_Op += 1

        combo_player = 0
        certificado = 0

    # mudança de fundo

    faixa = pygame.draw.line(
        tela, (255, 255, 255), (largura/2, 0), (largura/2, altura))
    player = pygame.draw.rect(tela, (255, 255, 255),
                              (playerx, posicao_player, 15, 50))
    boll = pygame.draw.rect(tela, (255, 255, 255), (bolaX, bolaY, 20, 20))
    oponent = pygame.draw.rect(
        tela, (255, 255, 255), (oponentX, oponentY, 15, 50))

    if pontos > 10 or pontosOp > 10:
        boll = pygame.draw.rect(tela, (255, 255, 255), (bolaX, bolaY, 20, 20))

    # BARREIRA JOGADOR
    if posicao_player <= 5:
        posicao_player = 5
    if posicao_player >= 420:
        posicao_player = 420

    # barreira oponente
    if oponentY <= 5:
        oponentY = 5
    if oponentY >= 420:
        oponentY = 420

    if boll.colliderect(oponent):
        bola_movX = -10
        colisao_player.play()
        combo_Op += 1
        certificado_Op += 1

    if boll.colliderect(player):
        bola_movX = 10
        colisao_player.play()
        combo_player += 1
        certificado += 1

    tela.blit(texto, [largura/2 - 40, altura/2])
    tela.blit(textoOp, [largura/2 + 16, altura/2])
    if combo_player > 0:
        tela.blit(combo_jogador, [200, 100])
    if combo_Op > 0:
        tela.blit(combo_enemy, [500, 100])

    pygame.display.update()
    #linha editada no github
