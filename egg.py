# coding: utf-8
import pygame
import os
import random
from score_bar import ScoreBar


__author__ = 'Eric-Nicolas'


class Egg(pygame.sprite.Sprite):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__()
        self.win_width, self.win_height = window.get_width(), window.get_height()
        self.image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'chocolate_egg.png')),
            (50, 50)
        )
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.win_width - self.image.get_width())
        self.rect.y = 0
        self.speed = 2

    def go_top(self, score_bar: ScoreBar) -> None:
        self.rect.y = 0
        self.rect.x = random.randint(0, self.win_width - self.image.get_width())
        if score_bar.is_winning() and score_bar.get_score() % 5 == 0:
            self.speed += 1

    def fall(self) -> None:
        self.rect.y += self.speed

    def has_fallen(self) -> bool:
        return self.rect.y >= self.win_height - self.image.get_height() - 75

    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.image, self.rect)
