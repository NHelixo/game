from sprites import *
from map import *
import pygame
from abc import ABC, abstractmethod
from random import randint


class Enemy:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.move_rand = 0
        self.x = 500
        self.y = 300

    @abstractmethod
    def spawn(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def moving(self):
        pass

    @abstractmethod
    def add_points(self):
        pass


class EnemyShooter(Enemy):
    def __init__(self, health, damage, speed, x, y):
        super().__init__(health, damage, speed)
        self.rect = pygame.Rect(x, y, enemy.get_width(), enemy.get_height())
        self.last_shot_time = 0
        self.shot_delay = 1000
        self.bullets = []
        self.target_reached = False
        self.last_collided = None

    def spawn(self):
        self.move_rand = randint(1, 4)
        self.target_reached = False
        print(f"Spawned with direction: {self.move_rand}")

    def attack(self, player):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shot_delay:
            bullet = pygame.Rect(self.x, self.y, 5, 5)
            self.bullets.append((bullet, self.move_rand))
            self.last_shot_time = current_time

        new_bullets = []
        for bullet, move_rand in self.bullets:
            if move_rand == 1: bullet.x -= 10
            elif move_rand == 2: bullet.x += 10
            elif move_rand == 3: bullet.y -= 10
            elif move_rand == 4: bullet.y += 10

            if bullet.colliderect(player.rect):
                player.take_damage(10)
                continue

            # Перевірка на зіткнення з блоками
            hit_wall = False
            for wall in rect_map_1:
                if bullet.colliderect(wall):
                    hit_wall = True
                    break

            if hit_wall:
                continue

            new_bullets.append((bullet, move_rand))
            pygame.draw.rect(screen, (255, 0, 0), bullet)

        self.bullets = new_bullets

    def moving(self):
        new_x, new_y = self.x, self.y
    
        # Рух відповідно до напрямку
        if self.move_rand == 1:
            new_x -= self.speed
        elif self.move_rand == 2:
            new_x += self.speed
        elif self.move_rand == 3:
            new_y -= self.speed
        elif self.move_rand == 4:
            new_y += self.speed
    
        # Створюємо прямокутник для нової позиції
        new_rect = pygame.Rect(new_x, new_y, enemy.get_width(), enemy.get_height())
    
        # Перевірка меж екрану
        if new_x <= 0 or new_x >= 940 or new_y <= 0 or new_y >= 531:
            self.target_reached = True
            self.last_collided = None
        elif self.check_collision(rect_map_1, new_rect):
            # Якщо зіткнення з блоком — змінити напрям
            self.target_reached = True
    
        if self.target_reached:
            old_direction = self.move_rand
            self.change_direction(exclude=[old_direction])
            self.target_reached = False
        else:
            self.x, self.y = new_x, new_y
    
        self.rect.x, self.rect.y = self.x, self.y
    
        # Відображення ворога
        screen.blit(enemy, (self.x, self.y))
    
        # Відображення здоров'я
        font = pygame.font.SysFont("Arial", 20)
        health_text = font.render(str(self.health), True, (255, 0, 0))
        screen.blit(health_text, (self.x, self.y - 20))

    def check_collision(self, blocks, rect):
        for block in blocks:
            if rect.colliderect(block):
                if self.last_collided != block:
                    self.last_collided = block
                    return True
        return False

    def add_points(self):
        return 10

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            pass

    def change_direction(self, exclude=[]):
        directions = [d for d in [1, 2, 3, 4] if d not in exclude]
        self.move_rand = randint(1, 4) if not directions else directions[randint(0, len(directions) - 1)]


class MeleeAttackEnemy(Enemy):
    def spawn(self):
        pass

    def attack(self):
        pass

    def moving(self):
        pass
    
    def add_points(self):
        return 15