from sprites import *
from map import *
import pygame


class Player:
    def __init__(self, health, damage, speed, x, y, rect_map):
        self.anim_count_walk = 0
        self.health = health
        self.damage = damage
        self.speed = speed
        self.bullets = []
        self.xp = 0
        self.rect = pygame.Rect(x, y, main_forward.get_width(), main_forward.get_height())
        self.rotate_index = 1
        self.fire_direction = [self.rect.x, self.rect.y + 10]
        self.player_direction = main_forward
        self.rect_map = rect_map  # Зберігаємо rect_map як атрибут

    def run(self):
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_a]:
            dx = -self.speed
            self.rotate_index = 1
            self.fire_direction = [self.rect.x, self.rect.y + 10]
            self.player_direction = main_left
        if keys[pygame.K_d]:
            dx = self.speed
            self.rotate_index = 2
            self.fire_direction = [self.rect.x + main_right.get_width(), self.rect.y + 10]
            self.player_direction = main_right
        if keys[pygame.K_w]:
            dy = -self.speed
            self.rotate_index = 3
            self.fire_direction = [self.rect.x + main_back.get_height() / 2, self.rect.y]
            self.player_direction = main_back
        if keys[pygame.K_s]:
            dy = self.speed
            self.rotate_index = 4
            self.fire_direction = [self.rect.x + main_forward.get_height() / 2, self.rect.y + main_forward.get_width()]
            self.player_direction = main_forward

        self.rect.x += dx
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 940:
            self.rect.x = 940

        if self.check_collision(self.rect_map):  # Використовуємо self.rect_map
            self.rect.x -= dx

        self.rect.y += dy
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 531:
            self.rect.y = 531

        if self.check_collision(self.rect_map):  # Використовуємо self.rect_map
            self.rect.y -= dy

        screen.blit(self.player_direction, (self.rect.x, self.rect.y))

    def check_collision(self, blocks):
        for block in blocks:
            if self.rect.colliderect(block):
                return True
        return False

    def fire(self, events, enemies):
        # Обробка події натискання на кнопку миші
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                bullet = pygame.Rect(self.fire_direction[0], self.fire_direction[1] + 20, 5, 5)
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
            for wall in self.rect_map:  # Використовуємо self.rect_map
                if bullet.colliderect(wall):
                    hit_wall = True
                    break

            if hit_wall:
                continue

            # Перевірка на зіткнення з ворогами
            hit_enemy = False
            for enemy in enemies:
                if bullet.colliderect(enemy.rect):
                    enemy.take_damage(10)
                    hit_enemy = True
                    break

            if hit_enemy:
                continue

            new_bullets.append((bullet, direction))
            pygame.draw.rect(screen, (255, 0, 0), bullet)

        self.bullets = new_bullets

    def take_damage(self, amount):
        self.health -= amount
        print(f"Player HP: {self.health}")

    def is_dead(self):
        return self.health <= 0