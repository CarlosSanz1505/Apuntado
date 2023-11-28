"""Script principal del aplicativo,
ejecuta el Juego.
"""

import pygame
from screens import *
from objects import *

# Parámetros del Programa
width, height = 900, 700

# Inicialización
pygame.init()
display = pygame.display.set_mode((width, height))

# Título e Icono de la Ventana
pygame.display.set_caption("Apuntado")
icon = pygame.image.load("PYGAME/images/icon.png")
pygame.display.set_icon(icon)

# Cargar el Fondo
bg = pygame.image.load("PYGAME/images/bg.png").convert()
bg = pygame.transform.scale(bg, (width, height))

# El aplicativo comienza en la Pantalla "Autenticacion"
screen = "Autenticacion"

# Ciclo del Juego
while True:
    # "Dibujar" el color de fondo del aplicativo
    display.blit(bg, (0, 0))

    # Si no se ha hecho click, no se acciona nada
    click_pos = (0, 0)
    pressed_key = ""

    # Recibir eventos
    for event in pygame.event.get():

        # Cerrar el Juego
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Click en la Pantalla,
        # se guarda la posición del mouse
        # para identificar el botón presionado
        if (event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1):
            click_pos = pygame.mouse.get_pos()
        
        if (event.type == pygame.KEYDOWN):
            pressed_key = event.unicode
    
    # Pantalla a mostrar
    match screen:
        case "Autenticacion":
            screen = autenticacion(display, click_pos)
        case "Crear Cuenta":
            screen = crear_cuenta(display, click_pos, pressed_key)
        case "TyC":
            screen = tyc(display, click_pos)
        case "Menu":
            screen = menu(display, click_pos)
        # OPCIONAL
        case "Cuenta":
            screen = cuenta(display, click_pos)
        case "Tokens":
            screen = tokens(display, click_pos)
        case "Personalizacion":
            screen = personalizacion(display, click_pos)
        case "Informacion":
            screen = informacion(display, click_pos)
        case "Bot":
            screen = bot(display, click_pos)
    
    # [para facilitar Debugging]
    button_menu = Button(width//2 - 100/2, height - 80, 100, 50,
                         "Menu", "Menu")
    display.blit(button_menu.image, button_menu.rect)
    if (button_menu.rect.collidepoint(click_pos)):
        screen = "Menu"

    pygame.display.update()
