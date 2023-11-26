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
                 to: str):
        
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 150, 70))
        pygame.draw.rect(self.image, (0, 0, 0), (0, 0, width, height), 2)
        font = pygame.font.Font(None, 36)
        text_render = font.render(text, True, (255, 255, 255))
        text_rect = text_render.get_rect(center=(width // 2, height // 2))
        self.image.blit(text_render, text_rect)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.to = to
