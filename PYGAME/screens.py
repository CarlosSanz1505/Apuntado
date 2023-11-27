"""Contiene las funciones que representan
cada pantalla del Juego.

Cada función 'dibuja' los elementos de su
respectiva pantalla y devuelve un `string`
indicando la pantalla a mostrar en el siguiente
frame.

PANTALLAS:
    ```
    "Autenticacion"
    "Crear Cuenta"
    "TyC"
    "Menu"
    "Cuenta"
    "Tokens"
    "Personalizacion"
    "Informacion"
    "Bot"
    ```
    """

import pygame
from objects import *

# Parámetros
width, height = 900, 500
bg_color = (150, 0, 50)

# CARLOS
def autenticacion(display: pygame.Surface,
                  click_pos: tuple[int]) -> str:
    
    # Contenido de la Pantalla
    buttons = [
        Button(width/2 - 100, height/2 - 80, 200, 50, "Iniciar Sesion", "Autenticacion"),
        Button(width/2 - 100, height/2 + 30, 200, 50, "Crear Cuenta", "TyC")
    ]

    # button_iniciar_sesion = Button(300, 100, 200, 50,
    #                                "Iniciar Sesion", "TyC")
    # button_crear_cuenta = Button(300, 300, 200, 50,
    #                              "Crear Cuenta", "TyC")
    
    for button in buttons:
        display.blit(button.image, button.rect)

    # display.blit(button_iniciar_sesion.image,
    #              button_iniciar_sesion.rect)
    # display.blit(button_crear_cuenta.image,
    #              button_crear_cuenta.rect)

    # Funcionalidad Botón de Iniciar Sesión
    for button in buttons:
        if (button.rect.collidepoint(click_pos)):
            return button.to

    # if (button_iniciar_sesion.rect.collidepoint(click_pos)):
    #     return "Menu"
    # if (button_crear_cuenta.rect.collidepoint(click_pos)):
    #     return "Crear Cuenta"
    
    return "Autenticacion"

# CARLOS
def crear_cuenta(display: pygame.Surface,
                 click_pos: tuple[int]) -> str:
    
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    name = font.render("[crear cuenta]", True, white)
    display.blit(name, (400, 100))

    return "Crear Cuenta"

# VICTOR
def tyc(display: pygame.Surface,
        click_pos: tuple[int]) -> str:
    
    # Borrador
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    name = font.render("[términos y condiciones]", True, white)
    display.blit(name, (400, 100))
    
    return "TyC"

# CARLOS
def menu(display: pygame.Surface,
         click_pos: tuple[int]) -> str:
    
    # Contenido de la Pantalla
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    game_title = font.render("APUNTADO", True, white)
    display.blit(game_title, (400, 200))

    # Botones
    buttons = [
        Button(10, 10, 150, 50, "Cuenta", "Cuenta"),
        Button(width - 160, 10, 150, 50, "Tokens", "Tokens"),
        Button(10, height - 60, 150, 50, "Personalizacion", "Personalizacion"),
        Button(width - 80, height - 80, 70, 70, "", "Informacion", "PYGAME/images/info_button.png")
    ]
    
    # Dibujar los botones
    for button in buttons:
        display.blit(button.image, button.rect)
    
    info = pygame.image.load("PYGAME/images/info_icon.png")
    info = pygame.transform.scale(info, (0.6*info.get_width(), 0.6*info.get_height()))
    display.blit(info, (width - 52, height - 65))

    # Recibir clicks en los botones
    for button in buttons:
        if (button.rect.collidepoint(click_pos)):
            return button.to

    return "Menu"

# (OPCIONAL) VICTOR
def cuenta(display: pygame.Surface,
           click_pos: tuple[int]) -> str:
    
    # Borrador
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    name = font.render("[cuenta]", True, white)
    display.blit(name, (400, 100))
    
    return "Cuenta"

# VICTOR
def tokens(display: pygame.Surface,
           click_pos: tuple[int]) -> str:
    
    # Borrador
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    name = font.render("[tokens]", True, white)
    display.blit(name, (400, 100))

    return "Tokens"

# VICTOR
def personalizacion(display: pygame.Surface,
           click_pos: tuple[int]):
    
    # Borrador
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    name = font.render("[personalizacion]", True, white)
    display.blit(name, (400, 100))

    return "Personalizacion"

# ??????
def informacion(display: pygame.Surface,
                click_pos: tuple[int]):
    
    # Borrador
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    name = font.render("[reglas y tutorial]", True, white)
    display.blit(name, (400, 100))

    return "Informacion"

# CARLOS
def bot(display: pygame.Surface,
           click_pos: tuple[int]):
    
    # Borrador
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    name = font.render("[bot]", True, white)
    display.blit(name, (400, 100))

    return "Bot"
