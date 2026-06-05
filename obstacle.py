import pygame
import random

from settings import *

class Obstacle:

    def __init__(self):

        self.width = random.randint(20, 40)
        self.height = random.randint(40, 70)

        self.x = WIDTH

        self.y = GROUND_Y - self.height

    def update(self, speed):

        self.x -= speed

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            BLACK,
            (self.x, self.y, self.width, self.height)
        )

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )