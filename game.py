import pygame
from player import *
from map import *

player = Player(100, 5, 4, 100, 100)
map = Map()

running = True
while running:
    screen.fill((0, 0, 0))

    # # Копія поточної позиції
    # new_player = player.copy()

    # # Перевіряємо колізії зі стінами
    # if not any(new_player.colliderect(wall) for wall in map.walls):
    #     player = new_player  # Якщо немає колізії, оновлюємо позицію

    player.run()
    map.generating_map()

    pygame.display.update()

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
