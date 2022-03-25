from tkinter import Menu
import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))

def main():
    menu = pygame_menu.Menu('Forca', 600, 400,
                           theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Iniciar')
    menu.add.button('Historico')
    menu.add.button('Sair', pygame_menu.events.EXIT)

    menu.mainloop(surface)


main()