import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))

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
    menu.add.button(' P1 vs IA')
    menu.add.button('P1 vs P2')
    menu.add.button('Voltar', main)
    menu.mainloop(surface)


main()