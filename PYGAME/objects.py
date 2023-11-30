"""Objetos básicos recurrentes en el
aplicativo.
"""

import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self,
                 x: int,
                 y: int,
                 width: int,
                 height: int,
                 text: str,
                 to: str,
                 style: str = "PYGAME/images/green_button.png",
                 font_size: int = 26):
        
        super().__init__()
        image = pygame.image.load(style).convert_alpha()
        self.image = pygame.transform.scale(image, (width, height))
        font = pygame.font.Font("PYGAME/fonts/Koulen-Regular.ttf", font_size)
        text_render = font.render(text, True, (255, 255, 255))
        text_rect = text_render.get_rect(center=(width // 2 - 5, height // 2 - 7))
        self.image.blit(text_render, text_rect)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.to = to
        self.text = text
        self.style = style


class TextField(pygame.sprite.Sprite):
    def __init__(self,
                 x: int,
                 y: int,
                 width: int,
                 height: int,
                 initial_text: str,
                 text: str,
                 style: str = "PYGAME/images/txt_field.png",
                 font_size: int = 20,
                 font_color: tuple[int] = (133, 133, 133),
                 is_selected: bool = False):
        
        super().__init__()
        image = pygame.image.load(style).convert_alpha()
        self.image = pygame.transform.scale(image, (width, height))
        font = pygame.font.Font("PYGAME/fonts/Kufam-Regular.ttf", font_size)
        self.text = text
        self.font_color = font_color
        text_render = font.render(self.text, True, font_color)
        text_rect = text_render.get_rect(topleft=(25, 10))
        self.image.blit(text_render, text_rect)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_selected = is_selected
        self.initial_text = initial_text
