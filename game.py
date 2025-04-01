import pygame
from player import *
from enemy import *
from map import *


player = Player(100, 5, 4, 100, 100)
enemies: list[EnemyShooter] = []
map = Map()

running = True
while running:
    screen.fill((0, 0, 50))

    player.run()
    if len(enemies) < 3:
        for _ in range(3 - len(enemies)):
            enemy = EnemyShooter(60, 5, 5)
            enemy.spawn()
            enemies.append(enemy)

    map.generating_map()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    for enemy in enemies:
        enemy.moving()

    pygame.display.update()
    clock.tick(30)

