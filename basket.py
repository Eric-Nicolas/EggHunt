# coding: utf-8
import pygame
import os


__author__ = 'Eric-Nicolas'


class Basket:
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__()
        self.image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'basket.png')),
            (100, 100)
        )
        self.x = (window.get_width() - self.image.get_width()) // 2
        self.y = window.get_height() - self.image.get_height() - 75
        self.x_change = 0

    def idle(self) -> None:
        self.x_change = 0

    def move_left(self) -> None:
        self.x_change = -5

    def move_right(self) -> None:
        self.x_change = 5

    def update(self) -> None:
        self.x += self.x_change

    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.image, (self.x, self.y))
