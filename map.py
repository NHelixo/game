import pygame
from sprites import *

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("game")


class Map:
    def __init__(self):
        pass

    def generating_map(self):
        screen.blit(wall, (400, 400))