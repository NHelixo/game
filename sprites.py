import pygame

player = pygame.image.load('sprites/player/player.png')

wall_1 = pygame.image.load('sprites/map/wall_1.png')
wall_2 = pygame.image.load('sprites/map/wall_2.png')

map_1 = [[wall_1, 300, 300],
         [wall_1, 360, 300],
         [wall_2, 500, 500]]
