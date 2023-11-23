import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 50, 80
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Card class
class Card(pygame.sprite.Sprite):
    def __init__(self, suit, rank):
        super().__init__()
        self.image = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
        self.image.fill(WHITE)
        pygame.draw.rect(self.image, BLACK, (0, 0, CARD_WIDTH, CARD_HEIGHT), 2)
        font = pygame.font.Font(None, 36)
        text = font.render(f"{rank} of {suit}", True, BLACK)
        self.image.blit(text, (5, 5))
        self.rect = self.image.get_rect()

# Button class
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, action):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        pygame.draw.rect(self.image, BLACK, (0, 0, width, height), 2)
        font = pygame.font.Font(None, 36)
        text_render = font.render(text, True, BLACK)
        text_rect = text_render.get_rect(center=(width // 2, height // 2))
        self.image.blit(text_render, text_rect)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action

# Function to create a deck of cards
def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [Card(suit, rank) for suit in suits for rank in ranks]
    return deck

# Function to draw the cards on the screen
def draw_cards(cards, screen):
    for i, card in enumerate(cards):
        card.rect.x = 20 + i * (CARD_WIDTH + 10)
        card.rect.y = 250
        screen.blit(card.image, card.rect)

# Function to draw the button on the screen
def draw_button(button, screen):
    screen.blit(button.image, button.rect)

# Function to display the login screen
def show_login_screen(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("Login Screen", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200))

    # Draw input boxes (for simplicity, just rectangles here)
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 100, 250, 200, 30), 2)
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 100, 300, 200, 30), 2)

    username_text = font.render("Username:", True, BLACK)
    screen.blit(username_text, (WIDTH // 2 - 150, 250))

    password_text = font.render("Password:", True, BLACK)
    screen.blit(password_text, (WIDTH // 2 - 150, 300))

    return pygame.Rect(WIDTH // 2 - 100, 250, 200, 30), pygame.Rect(WIDTH // 2 - 100, 300, 200, 30)

# Function to display the options screen
def show_options_screen(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("Options Screen", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200))

# Function to display the menu
def show_menu(screen):
    font = pygame.font.Font(None, 74)
    text = font.render("Card Game Menu", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200))

    font = pygame.font.Font(None, 36)

    # Start Game button
    start_game_text = font.render("Start Game", True, BLACK)
    start_game_rect = start_game_text.get_rect(center=(WIDTH // 2, 300))
    screen.blit(start_game_text, start_game_rect)

    # Options button
    options_text = font.render("Options", True, BLACK)
    options_rect = options_text.get_rect(center=(WIDTH // 2, 350))
    screen.blit(options_text, options_rect)

    # Quit button
    quit_text = font.render("Quit", True, BLACK)
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, 400))
    screen.blit(quit_text, quit_rect)

    return start_game_rect, options_rect, quit_rect

# Main login function
def login():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Card Game - Login")
    clock = pygame.time.Clock()

    username = ""
    password = ""
    active_input = "username"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Check the entered username and password
                    if username == "your_username" and password == "your_password":
                        return
                elif event.key == pygame.K_BACKSPACE:
                    if len(username) > 0 and active_input == "username":
                        username = username[:-1]
                    elif len(password) > 0 and active_input == "password":
                        password = password[:-1]
                elif event.unicode.isalnum() or event.unicode in "_-":
                    if active_input == "username" and len(username) < 20:
                        username += event.unicode
                    elif active_input == "password" and len(password) < 20:
                        password += event.unicode
                elif event.key == pygame.K_TAB:
                    # Switch active input field on Tab key press
                    active_input = "password" if active_input == "username" else "username"

        # Draw background
        screen.fill(WHITE)

        # Display login screen
        username_rect, password_rect = show_login_screen(screen)

        # Highlight the active input field
        if active_input == "username":
            pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 100, 250, 200, 30), 2)
        elif active_input == "password":
            pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 100, 300, 200, 30), 2)

        # Display entered username and password
        font = pygame.font.Font(None, 36)
        username_text = font.render(f"Username: {username}", True, BLACK)
        password_text = font.render(f"Password: {'*' * len(password)}", True, BLACK)

        screen.blit(username_text, (WIDTH // 2 - 150, 250))
        screen.blit(password_text, (WIDTH // 2 - 150, 300))

        pygame.display.flip()
        clock.tick(FPS)

# Main menu function
def main_menu():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Card Game - Main Menu")
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_game_rect.collidepoint(event.pos):
                    return True
                elif options_rect.collidepoint(event.pos):
                    options_menu()
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Draw background
        screen.fill(WHITE)

        # Display menu
        start_game_rect, options_rect, quit_rect = show_menu(screen)

        pygame.display.flip()
        clock.tick(FPS)

# Options menu function
def options_menu():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Card Game - Options")
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(event.pos):
                    return

        # Draw background
        screen.fill(WHITE)

        # Display options screen
        show_options_screen(screen)

        pygame.display.flip()
        clock.tick(FPS)

# Main game function
def main():
    login()
    
    if not main_menu():
        return

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Card Game")
    clock = pygame.time.Clock()

    # Create a deck of cards
    deck = create_deck()

    # Shuffle the deck
    random.shuffle(deck)

    # Player's hand
    player_hand = []

    # Deal initial hand (e.g., 5 cards)
    for _ in range(5):
        player_hand.append(deck.pop())

    # Create a button to go back to the menu
    back_to_menu_button = Button(20, 20, BUTTON_WIDTH, BUTTON_HEIGHT, "Back to Menu", "menu")

    # Sprite groups
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player_hand)
    all_sprites.add(back_to_menu_button)

    # Sprite groups
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player_hand)
    all_sprites.add(back_to_menu_button)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Check for button click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if back_to_menu_button.rect.collidepoint(pos):
                    return  # Go back to the menu

        # Draw background
        screen.fill(WHITE)

        # Draw player's hand
        draw_cards(player_hand, screen)

        # Draw the button
        draw_button(back_to_menu_button, screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
