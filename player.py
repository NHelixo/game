from sprites import *
from map import *
import pygame


class Player:
    def __init__(self, health, damage, speed, x, y):
        self.anim_count_walk = 0
        self.health = health
        self.damage = damage
        self.speed = speed
        self.x = x
        self.y = y

    def run(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_a]:
            self.x -= self.speed
        if self.keys[pygame.K_d]:
            self.x += self.speed
        if self.keys[pygame.K_w]:
            self.y -= self.speed
        if self.keys[pygame.K_s]:
            self.y += self.speed

        screen.blit(player, (self.x, self.y))

    def fire(self):
        pass