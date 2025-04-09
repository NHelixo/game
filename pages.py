import pygame
from game import player, enemies, screen, clock, font

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class MainMenu:
    def __init__(self):
        self.buttons = [
            pygame.Rect(375, 250, 250, 50),  # Кнопка "Play"
            pygame.Rect(375, 350, 250, 50),  # Кнопка "Settings"
        ]
        
    def draw(self):
        pygame.display.set_caption("Menu")
        screen.fill((0, 0, 50)) 
        menu_text = pygame.image.load('sprites\map\main_menu_text.png')
        menu_text = pygame.transform.scale(menu_text, (500, 100))

        screen.blit(menu_text, (255, 100))

        mouse_pos = pygame.mouse.get_pos()
        
        play_button_color = (0, 0, 80) if not self.buttons[0].collidepoint(mouse_pos) else (0, 100, 200)
        maps_button_color = (0, 0, 80) if not self.buttons[1].collidepoint(mouse_pos) else (0, 100, 200)

        pygame.draw.rect(screen, play_button_color, self.buttons[0])  # Play
        pygame.draw.rect(screen, maps_button_color, self.buttons[1])  # Settings

        draw_text("Play", font, (255, 255, 255), screen, 460, 260)
        draw_text("Settings", font, (255, 255, 255), screen, 430, 360)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttons[0].collidepoint(event.pos):  # Play
                return "play"
            elif self.buttons[1].collidepoint(event.pos):  # Maps
                return "maps"
            elif self.buttons[2].collidepoint(event.pos):  # Settings
                return "settings"
        return None
    
class Game_Over:
    def __init__(self):
        self.buttons = [
            pygame.Rect(375, 320, 250, 50),  # Кнопка "Play"
            pygame.Rect(375, 400, 250, 50),  # Quit
        ]

    def draw(self):
        screen.fill((0, 0, 50))
        
        game_over_text = pygame.image.load('sprites\map\game_over_text.png')  
        game_over_text = pygame.transform.scale(game_over_text, (500, 100))

        screen.blit(game_over_text, (255, 100))
        # draw_text("Game Over", font, (255, 255, 255), screen, 440, 150)

        mouse_pos = pygame.mouse.get_pos()

        mainmenu_button_color = (0, 0, 80) if not self.buttons[0].collidepoint(mouse_pos) else (0, 100, 200)
        quit_button_color = (0, 0, 80) if not self.buttons[1].collidepoint(mouse_pos) else (0, 100, 200)

        pygame.draw.rect(screen, mainmenu_button_color, self.buttons[0])  # Main Menu
        pygame.draw.rect(screen, (0, 0, 80), self.buttons[1])  # Quit

        draw_text("Main Menu", font, (255, 255, 255), screen, 410, 330)
        draw_text("Quit", font, (255, 255, 255), screen, 460, 410)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttons[0].collidepoint(event.pos):
                return "main_menu"
            elif self.buttons[1].collidepoint(event.pos):
                return "quit"
        return None

class PauseMenu:
    def __init__(self):
        self.buttons = [
            pygame.Rect(375, 250, 250, 50),  # Resume
            pygame.Rect(375, 320, 250, 50),  # Main Menu
            pygame.Rect(375, 390, 250, 50),  # Quit
        ]

    def draw(self):
        screen.fill((20, 20, 60))
        
        paused_text = pygame.image.load('sprites\map\paused_text.png')  
        paused_text = pygame.transform.scale(paused_text, (400, 100))

        screen.blit(paused_text, (305, 100))

        mouse_pos = pygame.mouse.get_pos()

        resume_button_color = (0, 0, 80) if not self.buttons[0].collidepoint(mouse_pos) else (0, 100, 200)
        mainmenu_button_color = (0, 0, 80) if not self.buttons[1].collidepoint(mouse_pos) else (0, 100, 200)
        quit_button_color = (0, 0, 80) if not self.buttons[2].collidepoint(mouse_pos) else (0, 100, 200)

        pygame.draw.rect(screen, resume_button_color, self.buttons[0])  # Play
        pygame.draw.rect(screen, mainmenu_button_color, self.buttons[1])  # Main Menu
        pygame.draw.rect(screen, quit_button_color, self.buttons[2])  # Quit

        draw_text("Resume", font, (255, 255, 255), screen, 433, 260)
        draw_text("Main Menu", font, (255, 255, 255), screen, 410, 330)
        draw_text("Quit", font, (255, 255, 255), screen, 460, 397)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttons[0].collidepoint(event.pos):
                return "resume"
            elif self.buttons[1].collidepoint(event.pos):
                return "main_menu"
            elif self.buttons[2].collidepoint(event.pos):
                return "quit"
        return None  

class Maps():
    def __init__(self):
        self.buttons = [
            pygame.Rect(300, 50, 400, 70),  # Кнопка "Map1"
            pygame.Rect(300, 140, 400, 70),  # Кнопка "Map2"
        ]

    def draw(self):
        screen.fill((20, 20, 60))
        
        mouse_pos = pygame.mouse.get_pos()

        map1_button_color = (0, 0, 80) if not self.buttons[0].collidepoint(mouse_pos) else (0, 100, 200)
        map2_button_color = (0, 0, 80) if not self.buttons[1].collidepoint(mouse_pos) else (0, 100, 200)

        pygame.draw.rect(screen, map1_button_color, self.buttons[0])  # Map1
        pygame.draw.rect(screen, map2_button_color, self.buttons[1])  # Map2

        draw_text("Map1", font, (255, 255, 255), screen, 490, 70)
        draw_text("Map2", font, (255, 255, 255), screen, 490, 160)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttons[0].collidepoint(event.pos):
                return "map1"
            elif self.buttons[1].collidepoint(event.pos):
                return "map2"
        return None  
