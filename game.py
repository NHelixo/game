import pygame
from player import *
from enemy import *
from map import *
from pages import *
from sprites import *

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)

# player = Player(100, 5, 4, 100, 100)
enemies: list[EnemyShooter] = []
# map = Map()

def update_game(player, enemies, events):
    player.fire(events, enemies)
    player.run()
    for enemy in enemies[:]:
        enemy.moving()
        enemy.attack(player)
        if enemy.health <= 0:
            player.xp += enemy.add_points()
            enemies.remove(enemy)

def draw_game(screen, player, enemies, selected_map):
    screen.fill((0, 0, 50))
    selected_map.generating_map()
    # HP/XP
    hp = font.render(f'HP: {player.health}', True, (255, 255, 255))
    xp = font.render(f'XP: {player.xp}', True, (255, 255, 255))
    screen.blit(hp, (10, 10))
    screen.blit(xp, (160, 10))


def spawn_enemy(x=0, y=0):
    enemy = EnemyShooter(60, 5, 5, x, y)
    enemy.spawn()
    return enemy

def game_loop(selected_map):
    global enemies  # щоб змінювати глобальний список ворогів і вони знову спавнились в початковій точці в новій грі
    enemies = []
    player = Player(10, 5, 4, 100, 100)
    # map = Map()
    pause_menu = PauseMenu()
    paused = False


    running = True
    while running:

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
            draw_game(screen, player, enemies, selected_map)
            update_game(player, enemies, events)

            # Перевірка чи гравець мертвий
            if player.is_dead():
                running = False    
                game_over = Game_Over()
                game_over.draw()
                hp_text = font.render(f'XP: {player.xp}', True, (255, 255, 255))
                screen.blit(hp_text, (450, 230))
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

        pygame.display.update()
        clock.tick(30)

def main():
    menu = MainMenu()
    maps = Maps()
    running = True
    while running:
        menu.draw()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            action = menu.handle_events(event)
            if action == "play":
                selected_map = None
                while selected_map is None:
                    maps.draw()
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return

                        action = maps.handle_events(event)
                        if action == "map1":
                            map = Map(rect_map_1, map_1)
                            selected_map = map
                            game_loop(selected_map)  # Виклик гри з вибраною мапою
                        elif action == "map2":
                            map = Map(rect_map_2, map_2)
                            selected_map = map
                            game_loop(selected_map)
            elif action == "settings":
                pass

            elif action == "quit":
                running = False
                pygame.quit()

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()