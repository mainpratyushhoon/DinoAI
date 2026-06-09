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

        upcoming = []

        for obs in self.obstacles:

            if obs.x + obs.width >= dino.x:
                upcoming.append(obs)

        if len(upcoming) == 0:
            return None

        obs1 = upcoming[0]

        if len(upcoming) > 1:
            obs2 = upcoming[1]
        else:
            obs2 = obs1

        return [

            (obs1.x - dino.x) / WIDTH,
            obs1.width / 100,
            obs1.height / 100,

            (obs2.x - dino.x) / WIDTH,
            obs2.width / 100,
            obs2.height / 100,

            self.game_speed / 20,

            dino.y / HEIGHT,

            dino.vel_y / 20,

            dino.jumps_used / 2
        ]