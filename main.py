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

clock = pygame.time.Clock()
FPS = 60


def main() -> None:
    basket = Basket(WIN)
    is_running = True

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            basket.move_left()
        elif keys_pressed[pygame.K_RIGHT]:
            basket.move_right()
        else:
            basket.idle()

        basket.update()

        WIN.fill(WHITE)
        WIN.blit(BACKGROUND_IMG, (0, 0))
        WIN.blit(GROUND_IMG, (0, 0))

        basket.draw(WIN)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
