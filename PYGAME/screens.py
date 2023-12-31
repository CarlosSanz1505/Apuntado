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

import random
import pygame
from objects import *

# Parámetros
width, height = 900, 700
bg_color = (150, 0, 50)
btn_width, btn_height = 180, 80


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

    form = [
        ["Nombre", "Carlos", False, (133, 133, 133)],
        ["Apellido", "Sanchez", False, (133, 133, 133)],
        ["Fecha de Nacimiento", "22/02/22", False, (133, 133, 133)],
        ["Teléfono Celular", "1324567890", False, (133, 133, 133)],
        ["Contraseña", "*contra1", False, (133, 133, 133)],
        ["Confirmar Contraseña", "*contra1", False, (133, 133, 133)],
        ["Apodo", "C4RL05", False, (133, 133, 133)]
    ]
    
    # Funcionalidad Botón de Iniciar Sesión
    for button in buttons:
        if (button.rect.collidepoint(click_pos)):
            return button.to, form
    
    return "Autenticacion", form


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
                file = open("PYGAME/jugadores.txt", "w")
                file.write("PYGAME/images/zombie.png "+" ".join([datum for datum in data]))
            return button.to, form, data, False

    return "Crear Cuenta", new_fields, None, error


def tyc(display: pygame.Surface,
        click_pos: tuple[int],
        scroll_offset) -> str:
    # Configuración del texto del título
    font_titulo = pygame.font.Font("PYGAME/fonts/Krub-Regular.ttf", 50)
    titulo = font_titulo.render("Términos y Condiciones", True, (255, 255, 255))
    display.blit(titulo, (width//2 - 270, 30))  # Ajusta las coordenadas según sea necesario

    # ventana = pygame.image.load("PYGAME/images/window.png").convert_alpha()
    # ventana = pygame.transform.scale(ventana, (845, 450))
    # display.blit(ventana, (30, 100))
    
    botones=[
        Button(20, height - 100, 85, 90, "", "Menu", "PYGAME/images/back_button.png"),
    ]
    # # Configuración del texto del contenido
    # font_contenido = pygame.font.Font(None, 20)
    # contenido = [
    #     "Al participar en este juego de apuestas de cartas, el jugador acepta cumplir con todos los terminos y condiciones establecidos",
    #     "a continuación:",
    #     "",
    #     "Edad Mínima: Solo se permite la participación de personas mayores de 18 años. Cualquier persona que no cumpla con este", 
    #     "requisito no podrá participar en el juego.",
    #     "",
    #     "Responsabilidad del Jugador: Cada jugador es responsable de su propia conducta y acciones durante el juego. El juego se basa",
    #     "en la honestidad y el fair play, por lo que cualquier intento de fraude o trampa resultará en la descalificación inmediata del",
    #     "jugador.",
    #     "",
    #     "Las apuestas conllevan riesgos financieros significativos y pueden resultar en adicción al juego, afectando negativamente la", 
    #     "salud mental, las relaciones personales y el desempeño laboral. Se recomienda practicar el juego de manera responsable y",
    #     "buscar ayuda si se experimentan problemas."
    # ]
    botones=[
        Button(300, 600, 120, 70, "Aceptar", "Menu", "PYGAME/images/green_button.png"),
        Button(500, 600, 120, 70, "Rechazar", "Autenticacion", "PYGAME/images/green_button.png")
    ]

    for boton in botones:
        display.blit(boton.image, boton.rect)
        if (boton.rect.collidepoint(click_pos)):
            return boton.to, scroll_offset
    
    # # Renderizar cada línea por separado y ajustar las posiciones
    # y_offset = 120
    # for linea in contenido:
    #     texto_linea = font_contenido.render(linea, True, (0,0,0))
    #     display.blit(texto_linea, (50, y_offset))
    #     y_offset += 30  # Ajusta el espaciado entre líneas según sea necesario
    
    font = pygame.font.Font("PYGAME/fonts/Kufam-Regular.ttf", 25)
    texto = [
        "Al participar en este juego de apuestas",
        "de cartas, el jugador acepta cumplir",
        "con todos los terminos y condiciones",
        "establecidos a continuación:",
        "",
        "Edad Mínima: Solo se permite la",
        "participación de personas mayores de",
        "18 años. Cualquier persona que no",
        "cumpla con este requisito no podrá",
        "participar en el juego.",
        "",
        "Responsabilidad del Jugador: Cada",
        "jugador es responsable de su propia",
        "conducta y acciones durante el juego.",
        "El juego se basa en la honestidad y el",
        "fair play, por lo que cualquier intento",
        "de fraude o trampa resultará en la",
        "descalificación inmediata del jugador.",
        "",
        "Las apuestas conllevan riesgos",
        "financieros significativos y pueden",
        "resultar en adicción al juego, afectando",
        "negativamente la salud mental, las",
        "relaciones personales y el desempeño",
        "laboral. Se recomienda practicar el",
        "juego de manera responsable y buscar",
        "ayuda si se experimentan problemas."
    ]

    # SCROLLABLE
    window = pygame.image.load("PYGAME/images/window.png").convert_alpha()
    window = pygame.transform.scale(window, (600, 450))
    display.blit(window, (width//2 - 300, 120))
    viewport_rect = pygame.Rect(0, 0, width, height-330)
    viewport_rect.y = scroll_offset
    virtual_surface = pygame.Surface([600, 1300], pygame.SRCALPHA, 32)
    virtual_surface = virtual_surface.convert_alpha()
    for i in range(len(texto)):
        line = font.render(texto[i], True, (0, 0, 0))
        virtual_surface.blit(line, (50, i*40))
    display.blit(virtual_surface, (width//2 - 300, 160), viewport_rect)

    page_bar = pygame.Rect(width//2 + 255, 160, 20, height-330)
    pygame.draw.rect(display, (150, 150, 150), page_bar)
    portion_bar = pygame.Rect(width//2 + 255, 160, 20, (height-330)*(height-330)/1300)
    portion_bar.y = 160 + 0.335*(scroll_offset/(1300-height)) * (height-portion_bar.height)
    pygame.draw.rect(display, (50, 50, 50,), portion_bar)
    
    # Verificar si la posición del clic está dentro de los límites del texto del título
    rectangulo_titulo = titulo.get_rect(topleft=(200, 50))
    if rectangulo_titulo.collidepoint(click_pos):
        # Agregar lógica para lo que sucede cuando se hace clic en el título
        print("Título de Información clicleado!")
    
    return "TyC", scroll_offset


def menu(display: pygame.Surface,
         click_pos: tuple[int]) -> str:
    
    # Título
    title = pygame.image.load("PYGAME/images/title.png").convert_alpha()
    title = pygame.transform.scale(title, (500, 140))
    display.blit(title, (width//2 - 250, 180))

    # Botones
    buttons = [
        Button(10, 15, 250, 100, "", "Menu", "PYGAME/images/blue_button.png"),
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
    file = open("PYGAME/jugadores.txt", "r")
    file.seek(0)
    avatar = file.read().split()[0]
    avatar = pygame.transform.scale(pygame.image.load(avatar).convert_alpha(), (90, 90))
    display.blit(avatar, (10, 10))

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


def cuenta(display: pygame.Surface,
           click_pos: tuple[int]) -> str:
    
    # Borrador
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    name = font.render("[cuenta]", True, white)
    display.blit(name, (400, 100))

    
    return "Cuenta"


def tokens(display: pygame.Surface,
           click_pos: tuple[int]) -> str:
    
    # Borrador
    # menu()
    ventana = pygame.image.load("PYGAME/images/window.png").convert_alpha()
    ventana = pygame.transform.scale(ventana, (600, 430))
    display.blit(ventana, (150, 120))

    # Icono
    icon = pygame.image.load("PYGAME/images/tokens_icon1.png.png").convert_alpha()
    # icon = pygame.transform.scale(icon, ())
    display.blit(icon, (width//2 - 80, 70))

    # Saldo
    deco1 = pygame.image.load("PYGAME/images/tokens_deco1.png").convert_alpha()
    deco1 = pygame.transform.scale(deco1, (70, 50))
    display.blit(deco1, (170, 150))
    font = pygame.font.Font("PYGAME/fonts/Koulen-Regular.ttf", 25)
    saldo = font.render("$10 000", True, (0, 0, 0))
    display.blit(saldo, (230, 155))

    # Paquetes
    small = "PYGAME/images/small_pkg.png"
    medium = "PYGAME/images/medium_pkg.png"
    big = "PYGAME/images/big_pkg.png"
    paquetes = [
        ["2K", small],
        ["10K", small],
        ["50K", medium],
        ["100K", medium],
        ["250K", big],
        ["1M", big]
    ]

    for i, paquete in enumerate(paquetes):
        block = pygame.image.load(paquete[1])
        block = pygame.transform.scale(block, (113, 104))
        display.blit(block, (250 + 133*(i%3), 220 + 150*(i//3)))
        font = pygame.font.Font("PYGAME/fonts/Krub-Regular.ttf", 20)
        price = font.render(paquete[0], True, (0, 0, 0))
        display.blit(price, (290 + 133*(i%3), 220 + 150*(i//3)))

    # Decoración
    deco = pygame.image.load("PYGAME/images/tokens_deco.png").convert_alpha()
    # deco = pygame.transform.scale(deco, ())
    display.blit(deco, (640, 420))

    # Botones
    buttons = [
        Button(250, 310, 113, 50, "$3 000", "Tokens"),
        Button(383, 310, 113, 50, "$5 000", "Tokens"),
        Button(516, 310, 113, 50, "$10 000", "Tokens"),
        Button(250, 460, 113, 50, "$80 000", "Tokens"),
        Button(383, 460, 113, 50, "$120 000", "Tokens"),
        Button(516, 460, 113, 50, "$200 000", "Tokens"),
        Button(20, height - 110, 90, 90, "", "Menu", "PYGAME/images/back_button.png"),
    ]

    for button in buttons:
        display.blit(button.image, button.rect)
        if (button.rect.collidepoint(click_pos)):
            return button.to

    return "Tokens"


def personalizacion(display: pygame.Surface,
                    click_pos: tuple[int],
                    avatar: str) -> tuple[str]:
    
    # Imagenes
    diseño1 = pygame.transform.scale(pygame.image.load("PYGAME/images/cartas1.png").convert_alpha(), (150, 150))
    diseño2 = pygame.transform.scale(pygame.image.load("PYGAME/images/cartas2.png").convert_alpha(), (150, 150))
    diseño3 = pygame.transform.scale(pygame.image.load("PYGAME/images/cartas3.png").convert_alpha(), (150, 150))
    display.blit(diseño1, (650,370))
    display.blit(diseño2, (150,370 ))
    display.blit(diseño3, (400,370))

    # Avatares
    avatares = [
        "PYGAME/images/vampire.png",
        "PYGAME/images/zombie.png",
        "PYGAME/images/mummy.png",
        "PYGAME/images/frankenstein.png",
        "PYGAME/images/joker.png"
    ]

    #Botones
    botones = [
        Button(350,600, btn_width, btn_height - 10, "GUARDAR", "Menu", font_size=22)
    ]
    botones += [Button(100 + 150*i, 160, 120, 120, "", "Personalizacion", avatar) for i, avatar in enumerate(avatares)]

    for boton in botones:
        display.blit(boton.image, boton.rect)
        if (boton.rect.collidepoint(click_pos)):
            if (boton.text == "GUARDAR"):
                file = open("PYGAME/jugadores.txt", "r+")
                file.seek(0)
                temp = " "+" ".join(file.readlines()[0].split()[1:])
                file.truncate(0)
                file.close()
                file = open("PYGAME/jugadores.txt", "w")
                jugador = avatar + temp
                file.write(jugador)
                file.close()
            else:
                avatar = str(boton.style)
            return boton.to, avatar
    
    return "Personalizacion", str(avatar)


def informacion(display: pygame.Surface, click_pos: tuple[int]) -> str:
    
    # Configuración del texto del título
    font_titulo = pygame.font.Font(None, 30)
    blanco = (255, 255, 255)
    titulo = font_titulo.render("Reglas y Tutorial", True, blanco)
    display.blit(titulo, (200, 50))  # Ajusta las coordenadas según sea necesario
    
    botones=[
        Button(20, height - 100, 85, 90, "", "Menu", "PYGAME/images/back_button.png"),
    ]
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
    botones=[
        Button(750, 20, 85, 90, "", "Menu", "PYGAME/images/back_button.png"),
    ]

    for boton in botones:
        display.blit(boton.image, boton.rect)
        if (boton.rect.collidepoint(click_pos)):
            return boton.to
    
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


def bot(display: pygame.Surface,
           click_pos: tuple[int],
           cards: list[pygame.Surface],
           hand_set: bool = False) -> tuple[str, bool]:
    
    # Mesa
    table = pygame.image.load("PYGAME/images/table.png").convert_alpha()
    table = pygame.transform.scale(table, (500, 440))
    display.blit(table, (width//2 - 250, 100))

    # Temporizador
    timer = pygame.image.load("PYGAME/images/timer.png").convert_alpha()
    timer = pygame.transform.scale(timer, (140, 100))
    display.blit(timer, (width - 150, height - 120))

    # Mano del Jugador
    hand = pygame.image.load("PYGAME/images/hand.png").convert_alpha()
    hand = pygame.transform.scale(hand, (550, 200))
    display.blit(hand, (width//2 - 290, 500))

    # Avatares
    # file = open("PYGAME/jugadores.txt", "r")
    # player = file.readline().split()[-1]
    file = open("PYGAME/jugadores.txt", "r")
    file.seek(0)
    player = file.read().split()[0]
    player = pygame.transform.scale(pygame.image.load(player).convert_alpha(), (90, 90))
    bot = pygame.image.load("PYGAME/images/frankenstein.png").convert_alpha()
    bot = pygame.transform.scale(bot, (100, 100))
    display.blit(player, (width//2 - 250, height//2))
    display.blit(bot, (width//2 + 115, height//2 - 200))
    font = pygame.font.Font("PYGAME/fonts/Kufam-Regular.ttf", 20)
    file.seek(0)
    player_name = file.read().split()[-1]
    player_name = font.render(player_name, True, (255, 255, 255))
    display.blit(player_name, (width//2 - 235, height//2 + 100))

    # Mazo de Cartas
    card_back1 = pygame.image.load("PYGAME/images/Cartas/Back Side 1.png").convert_alpha()
    card_back1 = pygame.transform.scale(card_back1, (70, 100))
    card_back2 = pygame.image.load("PYGAME/images/Cartas/Back Side 2.png").convert_alpha()
    card_back2 = pygame.transform.scale(card_back2, (70, 100))
    display.blit(card_back1, (width//2 - 50, width//2 - 200))
    display.blit(card_back2, (width//2 - 55, width//2 - 205))

    # Mano de Cartas
    nums = [f"{num:02}" for num in list(range(1, 62))]
    not_nums = ["38", "39", "40", "46", "47", "48", "54", "55", "56"]
    for num in not_nums:
        nums.remove(num)
    
    # Elegir cartas aleatoriamente, sin repetición
    if (len(cards) == 0):
        for i in range(10):
            num = random.choice(nums)
            nums.remove(num)
            path = "PYGAME/images/Cartas/Card-"+num+".png"
            card = pygame.image.load(path).convert_alpha()
            card = pygame.transform.scale(card, (50, 70))
            cards.append(card)
    
    for i, card in enumerate(cards):
        display.blit(card, (200 + 55*(i%5), 520 + 80*(i//5)))

    # Botones [Puntajes, Abandonar, Tocar, Ganar]
    buttons = [
        Button(10, 10, 110, 100, "", "Bot", "PYGAME/images/score_button.png"),
        Button(20, height - 110, 110, 100, "", "Menu", "PYGAME/images/exit_button.png"),
        Button(width//2 + 100, 530, 120, 80, "TOCAR", "Bot"),
        Button(width//2 + 100, 600, 120, 80, "GANAR", "Bot")
    ]
    for button in buttons:
        display.blit(button.image, button.rect)
        if (button.rect.collidepoint(click_pos)):
            if (button.to == "Menu"):
                cards = []
            return button.to, cards

    return "Bot", cards
