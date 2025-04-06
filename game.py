import pygame
from player import *
from enemy import *
from map import *

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)

player = Player(100, 5, 4, 100, 100)
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
            pygame.Rect(400, 250, 200, 50),  # Кнопка "Play"
            pygame.Rect(400, 350, 200, 50),  # Кнопка "Settings"
        ]
        
    def draw(self):
        pygame.display.set_caption("Menu")
        screen.fill((0, 0, 50)) 

        menu_text = font.render('Menu', True, (255, 255, 255))
        menu_rect = menu_text.get_rect(center=(500, 150))
        screen.blit(menu_text, menu_rect)

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
    

def spawn_enemy(x=0, y=0):
    enemy = EnemyShooter(60, 5, 5, x, y)
    enemy.spawn()
    return enemy

def game_loop():
    player = Player(100, 5, 4, 100, 100)
    map = Map()

    running = True
    while running:
        screen.fill((0, 0, 50))

        player.run()

        # Спавн ворогів
        while len(enemies) < 3:
            enemies.append(spawn_enemy())

        map.generating_map()

        # Обробка подій
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        player.fire(events)

        # Рух і атака ворогів
        for enemy in enemies:
            enemy.moving()
            enemy.attack(player)

        # Перевірка чи гравець мертвий
        if player.is_dead():
            print("Game Over!")
            running = False

        # Вивід HP
        hp_text = font.render(f'HP: {player.health}', True, (255, 255, 255))
        screen.blit(hp_text, (10, 10))

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
