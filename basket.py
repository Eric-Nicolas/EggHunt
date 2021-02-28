# coding: utf-8
import pygame
import os


__author__ = 'Eric-Nicolas'


class Basket(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'basket.png'))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.image, self.rect)
