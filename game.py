import pygame
from player import *
from enemy import *
from map import *


player = Player(100, 5, 4, 100, 100)
enemy = EnemyShooter(60, 5, 5)
map = Map()

running = True
while running:
    screen.fill((0, 0, 50))

    player.run()
    enemy.spawn()
    map.generating_map()

    pygame.display.update()

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

