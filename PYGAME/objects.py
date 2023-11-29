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


# class TextField(pygame.sprite.Sprite):
#     def __init__(self, x, y, width, height, initial_text, font_size=24, text_color=(0, 0, 0), background_color=(255, 255, 255)):
#         super().__init__()

#         self.font = pygame.font.Font(None, font_size)
#         self.text_color = text_color
#         self.background_color = background_color
#         self.is_selected = False

#         self.image = pygame.Surface((width, height))
#         self.image.fill(background_color)
#         pygame.draw.rect(self.image, text_color, (0, 0, width, height), 2)

#         self.rect = self.image.get_rect(topleft=(x, y))

#         self.initial_text = initial_text
#         self.current_text = initial_text

#     def update(self, events):
#         for event in events:
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 self.is_selected = self.rect.collidepoint(event.pos)
#                 if self.is_selected:
#                     self.current_text = ""

#             elif event.type == pygame.KEYDOWN and self.is_selected:
#                 if event.key == pygame.K_RETURN:
#                     # Handle the entered text (you can add your logic here)
#                     pass
#                 elif event.key == pygame.K_BACKSPACE:
#                     self.current_text = self.current_text[:-1]
#                 else:
#                     self.current_text += event.unicode

#         if not self.is_selected and not self.current_text:
#             self.current_text = self.initial_text

#         self.render_text()

#     def render_text(self):
#         self.image.fill(self.background_color)
#         pygame.draw.rect(self.image, self.text_color, (0, 0, self.rect.width, self.rect.height), 2)

#         text_surface = self.font.render(self.current_text, True, self.text_color)
#         text_rect = text_surface.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
#         self.image.blit(text_surface, text_rect)
