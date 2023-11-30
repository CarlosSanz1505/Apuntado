"""Script principal del aplicativo,
ejecuta el Juego.
"""

import os
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

# Determinar Pantalla al inicializar el aplicativo
# Si ya hay un jugador registrado -> Menu
if (os.stat("PYGAME/jugadores.txt").st_size == 0):
    screen = "Autenticacion"
else:
    screen = "Menu"

# Valores del Formulario en "Crear Cuenta"
# [TEXTO_DEFAULT, TEXTO_INGRESADO, IS_SELECTED, IS_DEFAULT]
# form = [
#     ["Nombre", "Nombre", False, (133, 133, 133)],
#     ["Apellido", "Apellido", False, (133, 133, 133)],
#     ["Fecha de Nacimiento", "Fecha de Nacimiento", False, (133, 133, 133)],
#     ["Teléfono Celular", "Teléfono Celular", False, (133, 133, 133)],
#     ["Contraseña", "Contraseña", False, (133, 133, 133)],
#     ["Confirmar Contraseña", "Confirmar Contraseña", False, (133, 133, 133)],
#     ["Apodo", "Apodo", False, (133, 133, 133)]
# ]
form = [
    ["Nombre", "Carlos", False, (133, 133, 133)],
    ["Apellido", "Sanchez", False, (133, 133, 133)],
    ["Fecha de Nacimiento", "22/02/22", False, (133, 133, 133)],
    ["Teléfono Celular", "1324567890", False, (133, 133, 133)],
    ["Contraseña", "*contra1", False, (133, 133, 133)],
    ["Confirmar Contraseña", "*contra1", False, (133, 133, 133)],
    ["Apodo", "C4RL05", False, (133, 133, 133)]
]
error = False

avatar = "PYGAME/images/zombie.png"

# Cartas del Juego
cards = []

# Ciclo del Juego
while True:
    # "Dibujar" el color de fondo del aplicativo
    display.blit(bg, (0, 0))

    # Si no se ha hecho click, no se acciona nada
    on_click = False
    click_pos = (0, 0)
    pressed_key = None

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
            on_click = True
        
        if (event.type == pygame.KEYDOWN):
            pressed_key = event
    
    # Pantalla a mostrar
    match screen:
        case "Autenticacion":
            screen = autenticacion(display, click_pos)
        case "Crear Cuenta":
            screen, form, data, error = crear_cuenta(display, on_click, click_pos, form, pressed_key, error)
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
            screen, avatar = personalizacion(display, click_pos, avatar)
        case "Informacion":
            screen = informacion(display, click_pos)
        case "Bot":
            screen, cards = bot(display, click_pos, cards)
    
    # # [para facilitar Debugging]
    # button_menu = Button(width//2 - 100/2, 20, 100, 50,
    #                      "Menu", "Menu")
    # display.blit(button_menu.image, button_menu.rect)
    # if (button_menu.rect.collidepoint(click_pos)):
    #     screen = "Menu"

    pygame.display.update()
