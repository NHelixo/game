from sprites import *
from map import *
import pygame


class Player:
    def __init__(self, health, damage, speed, x, y):
        self.anim_count_walk = 0
        self.health = health
        self.damage = damage
        self.speed = speed
        self.bullets = []
        self.rect = pygame.Rect(x, y, player.get_width(), player.get_height())
        self.rotate_index = ""

    def run(self):
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_a]:
            dx = -self.speed
            self.rotate_index = 1
        if keys[pygame.K_d]:
            dx = self.speed
            self.rotate_index = 2
        if keys[pygame.K_w]:
            dy = -self.speed
            self.rotate_index = 3
        if keys[pygame.K_s]:
            dy = self.speed
            self.rotate_index = 4

        self.rect.x += dx
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 940:
            self.rect.x = 940

        if self.check_collision(rect_map_1):
            self.rect.x -= dx

        self.rect.y += dy
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 531:
            self.rect.y = 531

        if self.check_collision(rect_map_1):
            self.rect.y -= dy

        screen.blit(player, (self.rect.x, self.rect.y))

    def check_collision(self, blocks):
        for block in blocks:
            if self.rect.colliderect(block):
                return True
        return False

    def fire(self):
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            bullet = pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, self.rect.y, 5, 5))
            direction = self.rotate_index
            self.bullets.append((bullet, direction))

        for bullet, direction in self.bullets:
            if direction == 1:
                bullet.x -= 10
            elif direction == 2:
                bullet.x += 10
            elif direction == 3:
                bullet.y -= 10
            elif direction == 4:
                bullet.y += 10

            pygame.draw.rect(screen, (255, 0, 0), bullet)
