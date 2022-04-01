import pygame as pg

branco = (255, 255, 255)
preto = (0, 0, 0)

def Desenho_da_Forca(surface, chance):
    pg.draw.rect(surface, branco, (0, 0, 1000, 600))
    pg.draw.line(surface, preto, (100,500), (100, 100), 10)
    pg.draw.line(surface, preto, (50, 500), (150, 500), 10)
    pg.draw.line(surface, preto, (100, 100), (300, 100), 10)
    pg.draw.line(surface, preto, (300, 100), (300, 150), 10)

    if chance >= 1:
        pg.draw.circle(surface, preto, (300, 200), 50, 10)
    if chance >= 2:
        pg.draw.line(surface, preto, (300, 250), (300, 350), 10)
    if chance >= 3:
        pg.draw.line(surface, preto, (300, 260), (225, 350), 10)
    if chance >= 4:
        pg.draw.line(surface, preto, (300, 260), (375, 350), 10)
    if chance >= 5:
        pg.draw.line(surface, preto, (300, 350), (375, 450), 10)
    if chance >=6:
        pg.draw.line(surface, preto, (300, 350), (225, 450), 10)

def Restart_button(surface, font_rb): 
    pg.draw.rect(surface, preto, (700, 100, 200, 65))
    text = font_rb.render('Restart', True, branco)
    surface.blit(text, (740, 120))

def camufla_palavra(palavra_escolhida, esconder_palavra, tentativas):
    esconder_palavra = palavra_escolhida
    for n in range(len(esconder_palavra)):
        if esconder_palavra[n:n+1] not in tentativas:
            esconder_palavra = esconder_palavra.replace(palavra_escolhida[n], '#')
    if '#' not in esconder_palavra:
        return 'Acertou'
    return esconder_palavra

def tentativa(tentativas, palavra_escolhida, letra, chance):
    if letra not in tentativas:
        tentativas.append(letra)
        if letra not in palavra_escolhida:
            chance += 1
    elif letra in tentativas:
        pass
    return tentativas, chance

def palavra_jogo(surface, palavra_camuflada, font):
    palavra = font.render(palavra_camuflada, True, preto)
    surface.blit(palavra, (200, 500))

def Restart_do_jogo(esconder_palavra, end_game,  chance, letra, tentativas, click_last_status, click, x, y):
    count = 0
    limite = len(esconder_palavra)
    for n in range(len(esconder_palavra)):
        if esconder_palavra[n] != '#':
            count += 1
    if count == limite and click_last_status == False and click[0] == True:
        tentativas = [' ', ' - ' ]
        end_game = True 
        chance = 0
        letra = ' '
    return end_game,  chance, tentativas, letra
