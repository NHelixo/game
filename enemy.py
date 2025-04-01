from sprites import *
from map import *
import pygame
from abc import ABC, abstractmethod


class Enemy:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.x = 0
        self.y = 0

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
        screen.blit(enemy, (200, 200))
        screen.blit(enemy, (300, 250))
        screen.blit(enemy, (500, 300))

    def attack(self):
        pass

    def moving(self):
        pass
    
    def add_points(self):
        pass


class MeleeAttackEnemy(Enemy):
    def spawn(self):
        pass

    def attack(self):
        pass

    def moving(self):
        pass
    
    def add_points(self):
        pass