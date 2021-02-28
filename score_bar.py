# coding: utf-8
import pygame


class ScoreBar:
    def __init__(self, window: pygame.Surface) -> None:
        self.color = (87, 64, 53)
        self.bg_color = (135, 147, 154)
        self.default_width = window.get_width() // 2
        self.thickness = 10

        self.score = 0
        self.width = self.default_width

    def get_score(self) -> int:
        return self.score

    def is_winning(self) -> bool:
        return self.width > self.default_width

    def is_empty(self) -> bool:
        return self.width <= 0

    def increase_score(self) -> None:
        self.score += 1

    def decrease_score(self) -> None:
        self.score -= 1

    def draw(self, window: pygame.Surface) -> None:
        self.width = self.default_width + self.score * 200
        pygame.draw.rect(window, self.bg_color, (0, 0, window.get_width(), self.thickness))
        pygame.draw.rect(window, self.color, (0, 0, self.width, self.thickness))
