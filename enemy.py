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
        self.x = 200
        self.y = 200

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
        self.target_reached = False  # Прапорець для перевірки, чи досягнуто протилежної сторони
        self.rect = pygame.Rect(x, y, enemy.get_width(), enemy.get_height())
        self.last_shot_time = 0
        self.shot_delay = 1000
        self.bullets = []
        self.last_collided = None

    def spawn(self):
        self.move_rand = randint(1, 4)
        self.target_reached = False
        print(f"Spawned with direction: {self.move_rand}")

    def attack(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot_time >= self.shot_delay:
            bullet = pygame.Rect(self.x, self.y, 5, 5)
            self.bullets.append((bullet, self.move_rand))
            self.last_shot_time = current_time

        for bullet, move_rand in self.bullets:
            if move_rand == 1:
                bullet.x -= 10
            elif move_rand == 2:
                bullet.x += 10
            elif move_rand == 3:
                bullet.y -= 10
            elif move_rand == 4:
                bullet.y += 10

            pygame.draw.rect(screen, (255, 0, 0), bullet)

    def moving(self):
        # Попереднє значення координат
        new_x = self.x
        new_y = self.y

        rect = pygame.Rect(new_x, new_y, enemy.get_width(), enemy.get_height())

        if self.check_collision(rect_map_1, rect):
            self.target_reached = True

        # Рух у поточному напрямку
        if self.move_rand == 1:
            new_x -= self.speed
        elif self.move_rand == 2:
            new_x += self.speed
        elif self.move_rand == 3:
            new_y -= self.speed
        elif self.move_rand == 4:
            new_y += self.speed

        # Перевірка, чи досягнуто протилежної сторони
        if self.move_rand == 1 and new_x <= 0:  # Вліво до x = 0
            new_x = 0
            self.target_reached = True
            self.last_collided = None
        elif self.move_rand == 2 and new_x >= 940:  # Вправо до x = 940
            new_x = 940
            self.target_reached = True
            self.last_collided = None
        elif self.move_rand == 3 and new_y <= 0:  # Вверх до y = 0
            new_y = 0
            self.target_reached = True
            self.last_collided = None
        elif self.move_rand == 4 and new_y >= 531:  # Вниз до y = 531
            new_y = 531
            self.target_reached = True
            self.last_collided = None

        # Якщо досягнуто протилежної сторони, змінюємо напрямок
        if self.target_reached:
            old_direction = self.move_rand
            exclude_directions = [old_direction]  # Виключаємо поточний напрямок
            self.change_direction(exclude=exclude_directions)
            self.target_reached = False  # Скидаємо прапорець
            print(f"Reached target. Old direction: {old_direction}, New direction: {self.move_rand}, Position: ({self.x}, {self.y})")

        # Оновлюємо координати
        else:
            self.x = new_x
            self.y = new_y

        # Відображаємо ворога
        screen.blit(enemy, (self.x, self.y))

    def check_collision(self, blocks, rect):
        for block in blocks:
            if rect.colliderect(block):
                if self.last_collided == block:
                    return False
                else:
                    self.last_collided = block
                    return True
        return False
    
    def add_points(self):
        return 10

    def change_direction(self, exclude=[]):
        possible_directions = [1, 2, 3, 4]
        for direction in exclude:
            if direction in possible_directions:
                possible_directions.remove(direction)
        if not possible_directions:
            possible_directions = [1, 2, 3, 4]
        self.move_rand = possible_directions[randint(0, len(possible_directions) - 1)]


class MeleeAttackEnemy(Enemy):
    def spawn(self):
        pass

    def attack(self):
        pass

    def moving(self):
        pass
    
    def add_points(self):
        return 15