# coding: utf-8
import pygame
import os


__author__ = 'Eric-Nicolas'


class Basket(pygame.sprite.Sprite):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__()
        self.win_width = window.get_width()
        self.image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'basket.png')),
            (100, 100)
        )
        self.rect = self.image.get_rect()
        self.rect.x = (self.win_width - self.image.get_width()) // 2
        self.rect.y = window.get_height() - self.image.get_height() - 75
        self.x_change = 0
        self.speed = 4

    def idle(self):
        self.x_change = 0

    def move_left(self) -> None:
        if self.rect.x > 0:
            self.x_change = -self.speed
        else:
            self.idle()

    def move_right(self) -> None:
        if self.rect.x < self.win_width - self.image.get_width():
            self.x_change = self.speed
        else:
            self.idle()

    def update(self) -> None:
        self.rect.x += self.x_change

    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.image, self.rect)
