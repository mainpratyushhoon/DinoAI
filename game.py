import pygame
import random

from settings import *
from dino import Dino
from obstacle import Obstacle


class Game:

    def __init__(self):

        self.dino = Dino()

        self.obstacles = []

        self.score = 0

        self.game_speed = 8

        self.spawn_timer = 0

        self.game_over = False

        self.font = pygame.font.SysFont(None, 40)

    def update(self):

        if self.game_over:
            return

        self.score += 1

        self.game_speed += 0.001

        self.dino.update()

        self.spawn_timer += 1

        if self.spawn_timer > random.randint(60, 120):

            self.obstacles.append(
                Obstacle()
            )

            self.spawn_timer = 0

        for obstacle in self.obstacles[:]:

            obstacle.update(self.game_speed)

            if obstacle.x + obstacle.width < 0:
                self.obstacles.remove(obstacle)

            if self.dino.get_rect().colliderect(
                obstacle.get_rect()
            ):
                self.game_over = True

    def draw(self, screen):

        screen.fill(WHITE)

        pygame.draw.line(
            screen,
            BLACK,
            (0, GROUND_Y),
            (WIDTH, GROUND_Y),
            3
        )

        self.dino.draw(screen)

        for obstacle in self.obstacles:
            obstacle.draw(screen)

        score_text = self.font.render(
            f"Score: {self.score}",
            True,
            BLACK
        )

        screen.blit(score_text, (20, 20))

        if self.game_over:

            text = self.font.render(
                "Game Over! Press R",
                True,
                BLACK
            )

            screen.blit(
                text,
                (350, 100)
            )

    def restart(self):

        self.__init__()