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
width, height = 900, 700
bg_color = (150, 0, 50)
btn_width, btn_height = 180, 80

# CARLOS
def autenticacion(display: pygame.Surface,
                  click_pos: tuple[int]) -> str:
    
    coin_bg = pygame.image.load("PYGAME/images/coin_bg.png").convert_alpha()
    coin_bg = pygame.transform.scale(coin_bg, (1.3*900, 1.3*565))
    display.blit(coin_bg, (-70, -30))

    buttons = [
        Button(width//2 - 100, height//2 - 80, 200, 80, "Iniciar Sesion", "Autenticacion"),
        Button(width//2 - 100, height//2 + 30, 200, 80, "Crear Cuenta", "Crear Cuenta")
    ]

    for button in buttons:
        display.blit(button.image, button.rect)

    # Funcionalidad Botón de Iniciar Sesión
    for button in buttons:
        if (button.rect.collidepoint(click_pos)):
            return button.to
    
    return "Autenticacion"

# CARLOS
def crear_cuenta(display: pygame.Surface,
                 on_click: bool,
                 click_pos: tuple[int],
                 form_values: list[list[str, bool]],
                 typed_key: pygame.event.Event,
                 error: bool) -> tuple[str, list, list]:
    
    # "Nueva Cuenta"
    font = pygame.font.Font("PYGAME/fonts/Krub-Regular.ttf", 60)
    name = font.render("Nueva Cuenta", True, (255, 255, 255))
    display.blit(name, (width//2 - 195, 60))

    # Campos de Texto
    fields = [TextField(150, 200 + 50*i, 600, 40,
                        form_values[i][0],
                        form_values[i][1],
                        is_selected=form_values[i][2],
                        font_color=form_values[i][3]) for i in range(7)]
    for field in fields:
        if (on_click):
            if (field.rect.collidepoint(click_pos)):
                field.is_selected = True
                field.text = ""
            else:
                field.is_selected = False
                if (field.text == ""):
                    field.text = field.initial_text
        
        if (typed_key != None):
            if (field.is_selected):
                if (typed_key.key == pygame.K_RETURN):
                    break
                if (typed_key.key == pygame.K_BACKSPACE):
                    field.text = field.text[:-1]
                if (typed_key.unicode.isprintable()):
                    field.text += typed_key.unicode
        
        if (field.text != field.initial_text):
            field.font_color = (0, 0, 0)
        else:
            field.font_color = (133, 133, 133)

        display.blit(field.image, field.rect)

    new_fields = [[field.initial_text,
                   field.text,
                   field.is_selected,
                   field.font_color] for i, field in enumerate(fields)]

    # Botones
    buttons = [
        Button(20, height - 80, 60, 60, "", "Autenticacion", "PYGAME/images/back_button1.png.png"),
        Button(width//2 - 100, height - 100, 200, 80, "Crear Cuenta", "TyC")
    ]

    data = [field.text for field in fields]

    if (error):
        font1 = pygame.font.Font("PYGAME/fonts/Kufam-Regular.ttf", 30)
        disclaimer = font1.render("*Debes diligenciar todos los datos*", True, (255, 124, 124))
        display.blit(disclaimer, (width//2 - 250, 560))

    for button in buttons:
        display.blit(button.image, button.rect)
        if (button.rect.collidepoint(click_pos)):
            form = [
                ["Nombre", "Nombre", False, (133, 133, 133)],
                ["Apellido", "Apellido", False, (133, 133, 133)],
                ["Fecha de Nacimiento", "Fecha de Nacimiento", False, (133, 133, 133)],
                ["Teléfono Celular", "Teléfono Celular", False, (133, 133, 133)],
                ["Contraseña", "Contraseña", False, (133, 133, 133)],
                ["Confirmar Contraseña", "Confirmar Contraseña", False, (133, 133, 133)],
                ["Apodo", "Apodo", False, (133, 133, 133)]
            ]
            if (button.to == "Autenticacion"):
                data = [None for i in range(7)]
            else:
                for field in fields:
                    if (field.text == field.initial_text):
                        return "Crear Cuenta", new_fields, None, True
                file = open("PYGAME/jugadores.txt", "a")
                file.write(" ".join([datum for datum in data]))
            return button.to, form, data, False

    return "Crear Cuenta", new_fields, None, error

# VICTOR
def tyc(display: pygame.Surface, click_pos: tuple[int]) -> str:
    # Configuración de la pantalla
    display.fill((0, 0, 0))  # Rellenar la pantalla con color negro
    
    # Configuración del texto del título
    font_titulo = pygame.font.Font(None, 40)
    blanco = (255, 255, 255)
    titulo = font_titulo.render("Términos y Condiciones", True, blanco)
    display.blit(titulo, (200, 50))  # Ajusta las coordenadas según sea necesario
    
    # Configuración del texto de los términos y condiciones
    font_contenido = pygame.font.Font(None, 30)
    contenido = (
        "1. Este es un ejemplo de términos y condiciones.\n"
        "2. Puedes personalizar este texto según tus necesidades.\n"
        "3. Asegúrate de cumplir con todas las políticas establecidas."
    )
    texto_contenido = font_contenido.render(contenido, True, blanco)
    display.blit(texto_contenido, (50, 120))  # Ajusta las coordenadas según sea necesario
    
    # Verificar si la posición del clic está dentro de los límites del texto del título
    rectangulo_titulo = titulo.get_rect(topleft=(200, 50))
    if rectangulo_titulo.collidepoint(click_pos):
        # Agregar lógica para lo que sucede cuando se hace clic en el título
        print("Título clicleado!")
    
    return "TyC"

# CARLOS
def menu(display: pygame.Surface,
         click_pos: tuple[int]) -> str:
    
    # Título
    title = pygame.image.load("PYGAME/images/title.png").convert_alpha()
    title = pygame.transform.scale(title, (500, 140))
    display.blit(title, (width//2 - 250, 180))

    # Botones
    buttons = [
        Button(10, 15, 250, 100, "", "Cuenta", "PYGAME/images/blue_button.png"),
        Button(width - 140, 60, 130, 70, "Tokens", "Tokens", "PYGAME/images/gold_button.png", font_size=22),
        Button(10, height - btn_height - 10, btn_width, btn_height - 10, "Personalizacion", "Personalizacion", font_size=22),
        Button(width - 90, height - 100, 85, 90, "", "Informacion", "PYGAME/images/info_button.png"),
        Button(width//2 - 195, height//2, 185, 185, "", "Bot", "PYGAME/images/bot_button.png"),
        Button(width//2 + 20, height//2, 185, 185, "", "Menu", "PYGAME/images/mp_button.png"),
    ]
    
    # Dibujar los botones
    for button in buttons:
        display.blit(button.image, button.rect)
    
    # Extra Cuenta
    joker = pygame.transform.scale(pygame.image.load("PYGAME/images/joker.png").convert_alpha(), (90, 90))
    mummy = pygame.transform.scale(pygame.image.load("PYGAME/images/mummy.png").convert_alpha(), (90, 90))
    vampire = pygame.transform.scale(pygame.image.load("PYGAME/images/vampire.png").convert_alpha(), (90, 90))
    zombie = pygame.transform.scale(pygame.image.load("PYGAME/images/zombie.png").convert_alpha(), (90, 90))
    frankenstein = pygame.transform.scale(pygame.image.load("PYGAME/images/frankenstein.png").convert_alpha(), (90, 90))
    display.blit(zombie, (10, 10))

    jugador = open("PYGAME/jugadores.txt", "r")
    nombre = jugador.readline().split()[-1]
    font = pygame.font.Font("PYGAME/fonts/Koulen-Regular.ttf", 24)
    nombre = font.render(nombre, True, (255, 255, 255))
    saldo = font.render("$10 000", True, (255, 255, 255))
    display.blit(nombre, (110, 20))
    display.blit(saldo, (110, 45))

    # Extra Tokens
    tokens_icon = pygame.transform.scale(pygame.image.load("PYGAME/images/tokens_icon.png").convert_alpha(), (120, 60))
    display.blit(tokens_icon, (width - 135, 15))

    # Extra Info
    info = pygame.image.load("PYGAME/images/info_icon.png")
    info = pygame.transform.scale(info, (0.6*info.get_width(), 0.6*info.get_height()))
    display.blit(info, (width - 60, height - 80))

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
    # menu()
    ventana = pygame.image.load("PYGAME/images/window.png").convert_alpha()
    ventana = pygame.transform.scale(ventana, (700, 500))
    display.blit(ventana, (100, 100))
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    name = font.render("Selecciona un paquete de tokens:", True, white)
    display.blit(name, (100, 100))

    #Imagenes paquetes
    tokens = pygame.transform.scale(pygame.image.load("PYGAME/images/tokens_icon.png").convert_alpha(), (200, 100))
    display.blit(tokens, (150,200))
    display.blit(tokens, (350,200))
    display.blit(tokens, (550,200))
    display.blit(tokens, (150,400))
    display.blit(tokens, (350,400))
    display.blit(tokens, (550,400))

    

    # Botones
    buttons = [
        Button(150,300, btn_width, btn_height - 10, "$10000", "$10000", font_size=22),
        Button(350,300, btn_width, btn_height - 10, "$20000", "$20000", font_size=22),
        Button(550,300, btn_width, btn_height - 10, "$30000", "$30000", font_size=22),
        Button(150,500, btn_width, btn_height - 10, "$40000", "$40000", font_size=22),
        Button(350,500, btn_width, btn_height - 10, "$50000", "$50000", font_size=22),
        Button(550,500, btn_width, btn_height - 10, "$60000", "$60000", font_size=22),
        Button(190, 170, 100, 50, "10k", "", "PYGAME/images/blue_button.png"),
        Button(390, 170, 100, 50, "20k", "", "PYGAME/images/blue_button.png"),
        Button(590, 170, 100, 50, "30k", "", "PYGAME/images/blue_button.png"),
        Button(190, 370, 100, 50, "40k", "", "PYGAME/images/blue_button.png"),
        Button(390, 370, 100, 50, "50k", "", "PYGAME/images/blue_button.png"),
        Button(590, 370, 100, 50, "60k", "", "PYGAME/images/blue_button.png"),
    ]

    for button in buttons:
        display.blit(button.image, button.rect)

    precio1 = font.render("10K", True, (0, 0, 0))
    display.blit(precio1, (250, 100))

    return "Tokens"

# VICTOR
def personalizacion(display: pygame.Surface,
           click_pos: tuple[int]):
    
    # Borrador
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    name = font.render("Selecciona tu nuevo diseño:", True, white)
    display.blit(name, (100, 100))

    #Imagenes
    joker = pygame.transform.scale(pygame.image.load("PYGAME/images/joker.png").convert_alpha(), (110, 110))
    mummy = pygame.transform.scale(pygame.image.load("PYGAME/images/mummy.png").convert_alpha(), (110, 110))
    vampire = pygame.transform.scale(pygame.image.load("PYGAME/images/vampire.png").convert_alpha(), (110, 110))
    zombie = pygame.transform.scale(pygame.image.load("PYGAME/images/zombie.png").convert_alpha(), (110, 110))
    frankenstein = pygame.transform.scale(pygame.image.load("PYGAME/images/frankenstein.png").convert_alpha(), (110, 110))
    # guardar=Button(550,500, btn_width, btn_height - 10, "Guardar", "Guardar", font_size=22),   
    display.blit(zombie, (250, 200))
    display.blit(joker,(400,200))
    display.blit(mummy,(550,200))
    display.blit(vampire,(100,200))
    display.blit(frankenstein,(700,200))
    diseño1 = pygame.transform.scale(pygame.image.load("PYGAME/images/cartas1.png").convert_alpha(), (150, 150))
    diseño2 = pygame.transform.scale(pygame.image.load("PYGAME/images/cartas2.png").convert_alpha(), (150, 150))
    diseño3 = pygame.transform.scale(pygame.image.load("PYGAME/images/cartas3.png").convert_alpha(), (150, 150))
    display.blit(diseño1, (650,370))
    display.blit(diseño2, (150,370 ))
    display.blit(diseño3, (400,370))

    #Botones
    botones=[
        Button(350,600, btn_width, btn_height - 10, "Guardar", "Menu", font_size=22),
        # Button()
    ]

    for boton in botones:
        display.blit(boton.image, boton.rect)
        if (boton.rect.collidepoint(click_pos)):
            return boton.to
    
    return "Personalizacion"

# ??????
def informacion(display: pygame.Surface, click_pos: tuple[int]) -> str:
    # Configuración de la pantalla
    display.fill((0, 0, 0))  # Rellenar la pantalla con color negro
    
    # Configuración del texto del título
    font_titulo = pygame.font.Font(None, 30)
    blanco = (255, 255, 255)
    titulo = font_titulo.render("Reglas y Tutorial", True, blanco)
    display.blit(titulo, (200, 50))  # Ajusta las coordenadas según sea necesario
    
    # Configuración del texto del contenido
    font_contenido = pygame.font.Font(None, 20)
    contenido = [
        "En su turno, un jugador puede realizar una de las siguientes acciones:",
        "-Arrastrar-Tirar-Tocar",
        "Para ganar, un jugador debe tener una de las siguientes combinaciones en su mano:",
        "-2 quintas (sucesión de 5 cartas consecutivas del mismo palo).",
        "-2 cuartas, siempre y cuando el puntaje de las cartas restantes en su mano sea inferior a 5.",
        "-3 ternas, siempre y cuando la carta sobrante sea menor o igual a 5.",
        "-2 ternas y una cuarta.",
        "Ganar una ronda:",
        "Cuando un jugador logra una combinación ganadora, debe declarar <<Apuntado>> y detener el juego.",
        "El jugador que gana la ronda suma 10 puntos a su puntaje total.",
        "Los demás jugadores deben mostrar sus manos y sumar los puntos de las cartas que no formen parte de las combinaciones",
        "ganadoras, agregando estos puntos como un valor negativo a su puntaje total.",
        "Puntaje:"
        "Cada carta tiene un valor según su número. Por ejemplo, los Ases valen 1 punto, las cartas del 2 al 10 valen su valor", 
        "nominal y las figuras (Jotas, Reinas y Reyes) valen 10 puntos cada una.",
        "Los jugadores suman sus puntos al final de cada ronda.",
        "Ganar el juego:",
        "El juego continúa hasta que un jugador alcanza o supera los 110 puntos positivos.",
        "Si en algún momento un jugador tiene un puntaje negativo inferior a -110, pierde el juego automáticamente.",
        "Si todos los jugadores tienen un puntaje negativo inferior a -110, el último jugador con el puntaje menos negativo gana."
    ]
    
    # Renderizar cada línea por separado y ajustar las posiciones
    y_offset = 120
    for linea in contenido:
        texto_linea = font_contenido.render(linea, True, blanco)
        display.blit(texto_linea, (50, y_offset))
        y_offset += 30  # Ajusta el espaciado entre líneas según sea necesario
    
    # Verificar si la posición del clic está dentro de los límites del texto del título
    rectangulo_titulo = titulo.get_rect(topleft=(200, 50))
    if rectangulo_titulo.collidepoint(click_pos):
        # Agregar lógica para lo que sucede cuando se hace clic en el título
        print("Título de Información clicleado!")
    
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
