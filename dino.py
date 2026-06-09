import pygame

from settings import *


class Dino:

    def __init__(self):
        self.jumps_used = 0

        self.max_jumps = 2
        self.image = pygame.image.load(
            "assets/dino.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (50, 50)
        )

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x = 100
        self.y = GROUND_Y - self.height

        self.vel_y = 0

        self.gravity = 0.8
        self.jump_force = -15

        self.on_ground = True

    def jump(self):

        if self.jumps_used < self.max_jumps:

            self.vel_y = self.jump_force

            self.jumps_used += 1

            self.on_ground = False

    def update(self):

        self.vel_y += self.gravity

        self.y += self.vel_y

        if self.y >= GROUND_Y - self.height:

            self.y = GROUND_Y - self.height

            self.jumps_used = 0

            self.vel_y = 0

            self.on_ground = True

    def draw(self, screen):

        screen.blit(
            self.image,
            (self.x, self.y)
        )

    def get_rect(self):

        return self.image.get_rect(
            topleft=(self.x, self.y)
        )