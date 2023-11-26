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
    
    # Contenido de la Pantalla
    # display.fill(bg_color)

    return "Crear Cuenta"

# VICTOR
def tyc(display: pygame.Surface,
        click_pos: tuple[int]) -> str:
    # Contenido de la Pantalla
    # display.fill(bg_color)
    
    return "TyC"

# CARLOS
def menu(display: pygame.Surface,
         click_pos: tuple[int]) -> str:
    
    # Contenido de la Pantalla
    # display.fill(bg_color)
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    game_title = font.render("APUNTADO", True, white)
    display.blit(game_title, (400, 200))

    return "Menu"

# (OPCIONAL) VICTOR
def cuenta(display: pygame.Surface,
           click_pos: tuple[int]):
    pass

# VICTOR
def tokens(display: pygame.Surface,
           click_pos: tuple[int]):
    pass

# VICTOR
def personalizacion(display: pygame.Surface,
           click_pos: tuple[int]):
    pass

# ??????
def informacion(display: pygame.Surface,
                click_pos: tuple[int]):
    pass

# CARLOS
def bot(display: pygame.Surface,
           click_pos: tuple[int]):
    pass
