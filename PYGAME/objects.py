"""Objectos básicos recurrentes en el
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
                 style: str = "PYGAME/images/button.png"):
        
        super().__init__()
        image = pygame.image.load(style).convert_alpha()
        self.image = pygame.transform.scale(image, (width, height))
        font = pygame.font.Font("PYGAME/fonts/Koulen-Regular.ttf", 26)
        text_render = font.render(text, True, (255, 255, 255))
        text_rect = text_render.get_rect(center=(width // 2, height // 2))
        self.image.blit(text_render, text_rect)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.to = to


class Text(pygame.sprite.Sprite):
    pass