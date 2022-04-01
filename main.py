from tkinter import Menu
import pygame
import pygame_menu
import random
from game import Desenho_da_Forca, camufla_palavra, palavra_jogo, tentativa

pygame.init()
surface = pygame.display.set_mode((1000, 600))
palavra = ''
font = pygame.font.SysFont('Courier New', 25)
font_rb = pygame.font.SysFont('Courier New', 15)

def playVsIa():
    palavras = [
    'JAVADRIGO',
    'CARRO',
    'CHATO',
    'CHORO',
    'VASCO'
    ]
    
    tentativas = [' ', ' - ']
    esconder_palavra = ""
    palavra_escolhida = random.choice(palavras)
    chance = 0 
    letra = ""
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                letra = str(pygame.key.name(event.key)).upper()
                print(letra)
        #jogo
        Desenho_da_Forca(surface, chance)
        esconder_palavra = camufla_palavra(palavra_escolhida, esconder_palavra, tentativas)
        tentativas, chance = tentativa(tentativas, palavra_escolhida, letra, chance)
        palavra_jogo(surface, esconder_palavra,font)

        if(esconder_palavra =='Acertou' and len(palavras) != 0):
            palavras.remove(palavra_escolhida)
            tentativas = [' ', ' - ']
            esconder_palavra = ""
            palavra_escolhida = random.choice(palavras)
            chance = 0 
            letra = ""
        if chance >= 6:
            main()
        pygame.display.update()

def play_vs_play():
    menu = pygame_menu.Menu('Escreva uma palavra chave', 600, 400,
                           theme=pygame_menu.themes.THEME_BLUE)
    
    menu.mainloop(surface)

def main():
    menu = pygame_menu.Menu('Forca', 600, 400,
                           theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Iniciar', mode_choice)
    menu.add.button('Historico')
    menu.add.button('Sair', pygame_menu.events.EXIT)

    menu.mainloop(surface)

def mode_choice():
    menu = pygame_menu.Menu('Escolha Uma opção', 600, 400,
                       theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button(' P1 vs IA',playVsIa)
    menu.add.button('P1 vs P2')
    menu.add.button('Voltar', main)
    menu.mainloop(surface)

main()