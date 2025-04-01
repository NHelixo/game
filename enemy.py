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
    def spawn(self):
        self.move_rand = randint(1, 4)

    def attack(self):
        pass

    def moving(self):
        if self.move_rand == 1:
            self.x -= self.speed
        elif self.move_rand == 2:
            self.x += self.speed
        elif self.move_rand == 3:
            self.y -= self.speed
        elif self.move_rand == 4:
            self.y += self.speed

        if self.x <= 0:
            self.x = 0
            self.spawn()
        if self.x >= 940:
            self.x = 940
            self.spawn()

        if self.y <= 0:
            self.y = 0
            self.spawn()
        if self.y >= 531:
            self.y = 531
            self.spawn()

        screen.blit(enemy, (self.x, self.y))
    
    def add_points(self):
        return 10


class MeleeAttackEnemy(Enemy):
    def spawn(self):
        pass

    def attack(self):
        pass

    def moving(self):
        pass
    
    def add_points(self):
        return 15