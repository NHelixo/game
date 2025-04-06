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
        self.rotate_index = 1

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

    def fire(self, events, enemies):
        # Обробка події натискання на кнопку миші
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                bullet = pygame.Rect(self.rect.x, self.rect.y, 5, 5)
                direction = self.rotate_index
                self.bullets.append((bullet, direction))

        new_bullets = []
        for bullet, direction in self.bullets:
            if direction == 1:
                bullet.x -= 10
            elif direction == 2:
                bullet.x += 10
            elif direction == 3:
                bullet.y -= 10
            elif direction == 4:
                bullet.y += 10

            # Перевірка на зіткнення з блоками
            hit_wall = False
            for wall in rect_map_1:
                if bullet.colliderect(wall):
                    hit_wall = True
                    break

            if hit_wall:
                continue

            # Перевірка на зіткнення з ворогами
            for enemy in enemies:
                if bullet.colliderect(enemy.rect):
                    enemy.take_damage(10)
                    break

            new_bullets.append((bullet, direction))
            pygame.draw.rect(screen, (255, 0, 0), bullet)

        self.bullets = new_bullets

    def take_damage(self, amount):
        self.health -= amount
        print(f"Player HP: {self.health}")

    def is_dead(self):
        return self.health <= 0