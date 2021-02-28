# coding: utf-8
import pygame
import os
import random


__author__ = 'Eric-Nicolas'


class Egg:
    def __init__(self, window: pygame.Surface) -> None:
        self.win_width, self.win_height = window.get_width(), window.get_height()
        self.image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'chocolate_egg.png')),
            (50, 50)
        )
        self.x = random.randint(0, self.win_width - self.image.get_width())
        self.y = 0
        self.speed = 2

    def fall(self) -> None:
        self.y += self.speed
        if self.y >= self.win_height - self.image.get_height() - 75:
            self.y = 0
            self.x = random.randint(0, self.win_width - self.image.get_width())

    def draw(self, window: pygame.Surface):
        window.blit(self.image, (self.x, self.y))
