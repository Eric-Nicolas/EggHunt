# coding: utf-8
import pygame
import os
from basket import Basket


__author__ = 'Eric-Nicolas'

pygame.init()

BACKGROUND_IMG = pygame.image.load(os.path.join('assets', 'background.jpg'))
GROUND_IMG = pygame.image.load(os.path.join('assets', 'ground.png'))

WHITE = (255, 255, 255)

WIDTH, HEIGHT = 800, 480
WIN: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Egg Hunt")

basket = Basket(WIN)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    WIN.fill(WHITE)
    WIN.blit(BACKGROUND_IMG, (0, 0))
    WIN.blit(GROUND_IMG, (0, 0))

    basket.draw(WIN)

    pygame.display.update()
