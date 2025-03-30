from sprites import *
from map import *
import pygame


class Player:
    def __init__(self, health, damage, speed, x, y):
        self.anim_count_walk = 0
        self.health = health
        self.damage = damage
        self.speed = speed
        self.rect = pygame.Rect(x, y, player.get_width(), player.get_height())

    def run(self):
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_s]:
            dy = self.speed

        self.rect.x += dx
        if self.check_collision(rect_map_1):
            self.rect.x -= dx

        self.rect.y += dy
        if self.check_collision(rect_map_1):
            self.rect.y -= dy

        screen.blit(player, (self.rect.x, self.rect.y))

    def check_collision(self, blocks):
        for block in blocks:
            if self.rect.colliderect(block):
                return True
        return False

    def fire(self):
        pass