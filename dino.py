import pygame
from settings import *

class Dino:
    def __init__(self):

        self.width = 40
        self.height = 50

        self.x = 100
        self.y = GROUND_Y - self.height

        self.vel_y = 0

        self.gravity = 0.8
        self.jump_force = -15

        self.on_ground = True

    def jump(self):

        if self.on_ground:
            self.vel_y = self.jump_force
            self.on_ground = False

    def update(self):

        self.vel_y += self.gravity
        self.y += self.vel_y

        if self.y >= GROUND_Y - self.height:

            self.y = GROUND_Y - self.height

            self.vel_y = 0

            self.on_ground = True

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