# coding: utf-8
import pygame
import os
from basket import Basket
from egg import Egg
from score_bar import ScoreBar


__author__ = 'Eric-Nicolas'


class Game:
    def __init__(self):
        pygame.init()

        ICON_IMG = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'chocolate.png')),
            (32, 32)
        )
        self._BACKGROUND_IMG = pygame.image.load(os.path.join('assets', 'background.jpg'))
        self.GROUND_IMG = pygame.image.load(os.path.join('assets', 'ground.png'))

        self._BLACK = (0, 0, 0)
        self._WHITE = (255, 255, 255)

        self._WIDTH, self._HEIGHT = 800, 480
        self._WIN = pygame.display.set_mode((self._WIDTH, self._HEIGHT))
        pygame.display.set_caption("Egg Hunt")
        pygame.display.set_icon(ICON_IMG)

        self.FONT = pygame.font.Font(None, 60)

        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.basket = Basket(self._WIN)
        self.egg = Egg(self._WIN)
        self.score_bar = ScoreBar(self._WIN)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        if not self.score_bar.is_empty():
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT]:
                self.basket.move_left()
            elif keys_pressed[pygame.K_RIGHT]:
                self.basket.move_right()
            else:
                self.basket.idle()

            self.basket.update()
            self.egg.fall()

            # Collision
            if pygame.sprite.collide_rect(self.basket, self.egg):
                self.egg.go_top(self.score_bar)
                self.score_bar.increase_score()
            elif self.egg.has_fallen():
                self.egg.go_top(self.score_bar)
                self.score_bar.decrease_score()

    def draw_background(self):
        self._WIN.fill(self._WHITE)
        self._WIN.blit(self._BACKGROUND_IMG, (0, 0))
        self._WIN.blit(self.GROUND_IMG, (0, 0))

    def draw_entities(self):
        self.basket.draw(self._WIN)
        self.egg.draw(self._WIN)
        self.score_bar.draw(self._WIN)

    def run(self):
        timer = 0
        is_running = True

        while is_running:
            self.check_event()
            self.update()
            self.draw_background()

            if not self.score_bar.is_empty():
                self.draw_entities()
            else:
                # Show game over for 3 seconds
                self.game_over()
                timer += 1
                if timer > self.FPS * 2:
                    is_running = False

            pygame.display.update()
            self.clock.tick(self.FPS)

    def game_over(self):
        label: pygame.Surface = self.FONT.render("Game Over", True, self._BLACK)
        self._WIN.blit(label, (
            (self._WIDTH - label.get_width()) // 2,
            (self._HEIGHT - label.get_height()) // 2
        ))
