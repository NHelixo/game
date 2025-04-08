import pygame
from sprites import *

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("game")


class Map:
    def generating_map(self):
        for rect in rect_map_1:
            pygame.draw.rect(screen, (0, 0, 0), rect)
            
        for sprite in map_1:
            screen.blit(sprite[0], (sprite[1], sprite[2]))