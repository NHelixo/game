import pygame
from sprites import *

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("game")


class Map:
    def __init__(self, rect_map, map):
        self.rect_map = rect_map
        self.map = map

    def generating_map(self):
        for rect in self.rect_map:
            pygame.draw.rect(screen, (0, 0, 0), rect)

        for sprite in self.map:
            screen.blit(sprite[0], (sprite[1], sprite[2]))
