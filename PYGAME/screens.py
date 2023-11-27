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
    button_iniciar_sesion = Button(300, 100, 200, 50,
                                   "Iniciar Sesion", "TyC")
    button_crear_cuenta = Button(300, 300, 200, 50,
                                 "Crear Cuenta", "TyC")
    display.blit(button_iniciar_sesion.image,
                 button_iniciar_sesion.rect)
    display.blit(button_crear_cuenta.image,
                 button_crear_cuenta.rect)

    # Funcionalidad Botón de Iniciar Sesión
    if (button_iniciar_sesion.rect.collidepoint(click_pos)):
        return "Menu"
    if (button_crear_cuenta.rect.collidepoint(click_pos)):
        return "Crear Cuenta"
    
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
    button_cuenta = Button(10, 10, 150, 50,
                           "Cuenta", "Cuenta")
    button_tokens = Button(900-10-150, 10, 150, 50,
                           "Tokens", "Tokens")
    button_pers = Button(10, 500-10-50, 150, 50,
                         "Personalizacion", "Personalizacion")
    button_info = Button(900-10-150, 500-10-50, 150, 50,
                         "Informacion", "Informacion")
    display.blit(button_cuenta.image,
                 button_cuenta.rect)
    display.blit(button_tokens.image,
                 button_tokens.rect)
    display.blit(button_pers.image,
                 button_pers.rect)
    display.blit(button_info.image,
                 button_info.rect)

    name = font.render("[menu]", True, white)
    display.blit(name, (400, 100))

    if (button_cuenta.rect.collidepoint(click_pos)):
        return "Cuenta"
    if (button_tokens.rect.collidepoint(click_pos)):
        return "Tokens"
    if (button_pers.rect.collidepoint(click_pos)):
        return "Personalizacion"
    if (button_info.rect.collidepoint(click_pos)):
        return "Informacion"

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
