# coding: utf-8
import pygame


class ScoreBar:
    def __init__(self, window):
        self.color = (87, 64, 53)
        self.bg_color = (135, 147, 154)
        self.default_width = window.get_width() // 2
        self.thickness = 10

        self.score = 0
        self.width = self.default_width

    def get_score(self):
        return self.score

    def is_winning(self):
        return self.width > self.default_width

    def is_empty(self):
        return self.width <= 0

    def increase_score(self):
        self.score += 1

    def decrease_score(self):
        self.score -= 1

    def draw(self, window):
        self.width = self.default_width + self.score * 200
        pygame.draw.rect(window, self.bg_color, (0, 0, window.get_width(), self.thickness))
        pygame.draw.rect(window, self.color, (0, 0, self.width, self.thickness))
