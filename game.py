import pygame
import random

from settings import *
from obstacle import Obstacle


class Game:

    def __init__(self):

        self.obstacles = []

        self.score = 0

        self.game_speed = 8

        self.spawn_timer = 0

        self.font = pygame.font.SysFont(None, 40)

    def update(self):

        self.score += 1

        if self.score % 100 == 0:
            self.game_speed += 1

        self.spawn_timer += 1

        if self.spawn_timer > random.randint(25, 170):

            self.obstacles.append(
                Obstacle()
            )

            self.spawn_timer = 0

        for obstacle in self.obstacles[:]:

            obstacle.update(self.game_speed)

            if obstacle.x + obstacle.width < 0:
                self.obstacles.remove(obstacle)

    def draw(self, screen):

        screen.fill(WHITE)

        pygame.draw.line(
            screen,
            BLACK,
            (0, GROUND_Y),
            (WIDTH, GROUND_Y),
            3
        )

        for obstacle in self.obstacles:
            obstacle.draw(screen)

        score_text = self.font.render(
            f"Score: {self.score}",
            True,
            BLACK
        )

        screen.blit(score_text, (20, 20))

    def get_state(self, dino):

        if len(self.obstacles) == 0:
            return None

        next_obstacle = self.obstacles[0]

        return [
            (next_obstacle.x - dino.x) / WIDTH,
            next_obstacle.width / 100,
            next_obstacle.height / 100,
            self.game_speed / 20,
            dino.y / HEIGHT,
            dino.vel_y / 20
        ]