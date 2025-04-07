import pygame
from player import *
from enemy import *
from map import *

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)

#player = Player(100, 5, 4, 100, 100)
enemies: list[EnemyShooter] = []
map = Map()

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
        settings_button_color = (0, 0, 80) if not self.buttons[1].collidepoint(mouse_pos) else (0, 100, 200)

        pygame.draw.rect(screen, play_button_color, self.buttons[0])  # Play
        pygame.draw.rect(screen, settings_button_color, self.buttons[1])  # Settings

        draw_text("Play", font, (255, 255, 255), screen, 460, 260)
        draw_text("Settings", font, (255, 255, 255), screen, 430, 360)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttons[0].collidepoint(event.pos):  # Play
                return "play"
            elif self.buttons[1].collidepoint(event.pos):  # Settings
                return "settings"
        return None
    
class Game_Over:
    def __init__(self):
        self.buttons = [
            pygame.Rect(375, 250, 250, 50),  # Кнопка "Play"
            pygame.Rect(375, 350, 250, 50),  # Quit
        ]

    def draw(self):
        screen.fill((0, 0, 50))
        
        game_over_text = pygame.image.load('sprites\map\game_over_text.png')  
        game_over_text = pygame.transform.scale(game_over_text, (500, 100))

        screen.blit(game_over_text, (255, 100))
        # draw_text("Game Over", font, (255, 255, 255), screen, 440, 150)

        mouse_pos = pygame.mouse.get_pos()

        # mainmenu_button_color = (0, 0, 80) if not self.buttons[0].collidepoint(mouse_pos) else (0, 100, 200)
        # quit_button_color = (0, 0, 80) if not self.buttons[1].collidepoint(mouse_pos) else (0, 100, 200)

        pygame.draw.rect(screen, (0, 0, 80), self.buttons[0])  # Main Menu
        pygame.draw.rect(screen, (0, 0, 80), self.buttons[1])  # Quit

        draw_text("Main Menu", font, (255, 255, 255), screen, 410, 260)
        draw_text("Quit", font, (255, 255, 255), screen, 460, 360)

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

        screen.blit(paused_text, (255, 100))
        # draw_text("Paused", font, (255, 255, 255), screen, 440, 150)

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


def spawn_enemy(x=0, y=0):
    enemy = EnemyShooter(60, 5, 5, x, y)
    enemy.spawn()
    return enemy

def game_loop():
    global enemies  # щоб змінювати глобальний список ворогів і вони знову спавнились в початковій точці в новій грі
    enemies = []
    player = Player(20, 5, 4, 100, 100)
    map = Map()
    pause_menu = PauseMenu()
    paused = False
    running = True

    running = True
    while running:
        screen.fill((0, 0, 50))

        player.run()

        # Спавн ворогів
        while len(enemies) < 3:
            enemies.append(spawn_enemy())

    
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = not paused

            if paused:
                action = pause_menu.handle_events(event)
                if action == "resume":
                    paused = False
                elif action == "main_menu":
                    return  # Exit to main menu
                elif action == "quit":
                    pygame.quit()
                    return
                
        if paused:
            pause_menu.draw()
        else:
            map.generating_map()
            player.fire(events, enemies)

        # Рух і атака ворогів
        for enemy in enemies:
            enemy.moving()
            enemy.attack(player)
            if enemy.health <= 0:
                player.xp += enemy.add_points()
                enemies.remove(enemy)


            # Перевірка чи гравець мертвий
            if player.is_dead():
                running = False    
                game_over = Game_Over()
                game_over.draw()  
                pygame.display.update()

                # Обробка подій для екрана Game Over
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return

                        action = game_over.handle_events(event)
                        if action == "main_menu":
                            return  # Повернутися в головне меню
                        elif action == "quit":
                            pygame.quit()
                            return
                
                        


        # Вивід HP
        hp_text = font.render(f'HP: {player.health}', True, (255, 255, 255))
        screen.blit(hp_text, (10, 10))

        # Вивід XP
        hp_text = font.render(f'XP: {player.xp}', True, (255, 255, 255))
        screen.blit(hp_text, (160, 10))

        pygame.display.update()
        clock.tick(30)

def main():
    menu = MainMenu()
    running = True
    while running:
        menu.draw()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            action = menu.handle_events(event)
            if action == "play":
                game_loop()  
            elif action == "quit":
                running = False
                pygame.quit()

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
