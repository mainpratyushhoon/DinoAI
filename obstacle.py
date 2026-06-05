import pygame
import random

from settings import *


class Obstacle:

    def __init__(self):

        cactus_types = [
            ("assets/smallcactus.png", (30, 50)),
            ("assets/tallcactus.png", (35, 70)),
            ("assets/twocactus.png", (60, 50))
        ]

        filename, size = random.choice(cactus_types)

        self.image = pygame.image.load(
            filename
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            size
        )

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x = WIDTH

        self.y = GROUND_Y - self.height

    def update(self, speed):

        self.x -= speed

    def draw(self, screen):

        screen.blit(
            self.image,
            (self.x, self.y)
        )

    def get_rect(self):

        return self.image.get_rect(
            topleft=(self.x, self.y)
        )