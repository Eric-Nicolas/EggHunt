# coding: utf-8
import pygame
import os


__author__ = 'Eric-Nicolas'


class Basket(pygame.sprite.Sprite):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__()
        self.image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'basket.png')),
            (100, 100)
        )
        self.rect = self.image.get_rect()
        self.rect.x = (window.get_width() - self.image.get_width()) // 2
        self.rect.y = window.get_height() - self.image.get_height() - 75

    def move_left(self) -> None:
        self.rect.x -= 1

    def move_right(self) -> None:
        self.rect.x += 1

    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.image, self.rect)
