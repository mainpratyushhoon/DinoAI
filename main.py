import pygame

from settings import *
from game import Game
from ai.neural_network import NeuralNetwork

brain = NeuralNetwork()
pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Dino AI"
)

clock = pygame.time.Clock()

game = Game()

running = True

while running:

    clock.tick(FPS)

    state = game.get_state()
    if state is not None:

        decision = brain.forward(state)
        print(decision)
        if decision > 0.5:
            game.dino.jump()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                game.dino.jump()

            if event.key == pygame.K_r:
                game.restart()

    game.update()

    game.draw(screen)

    pygame.display.flip()

pygame.quit()