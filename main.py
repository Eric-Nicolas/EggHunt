# coding: utf-8
import pygame
import os


pygame.init()

BACKGROUND_IMG = pygame.image.load(os.path.join('assets', 'background.jpg'))
GROUND_IMG = pygame.image.load(os.path.join('assets', 'ground.png'))

WIDTH, HEIGHT = 800, 480
WIN: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Egg Hunt")

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    WIN.blit(BACKGROUND_IMG, (0, 0))
    WIN.blit(GROUND_IMG, (0, 0))
    pygame.display.update()
