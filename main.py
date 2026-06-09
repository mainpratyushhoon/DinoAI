import pygame

from settings import *
from game import Game
from ai.agent import Agent


def next_generation(old_agents):

    best = max(
        old_agents,
        key=lambda a: a.fitness
    )

    print(
        f"Best fitness: {best.fitness}"
    )

    new_agents = [
        Agent(best.brain.copy())
    ]

    for _ in range(len(old_agents) - 1):

        brain = best.brain.copy()

        brain.mutate()

        new_agents.append(
            Agent(brain)
        )

    return new_agents


pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Dino AI"
)

clock = pygame.time.Clock()

POPULATION_SIZE = 100

generation = 1

agents = [
    Agent()
    for _ in range(POPULATION_SIZE)
]

game = Game()

font = pygame.font.SysFont(
    None,
    36
)

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    game.update()

    for agent in agents:

        if not agent.alive:
            continue

        state = game.get_state(
            agent.dino
        )

        if state is not None:

            decision = agent.brain.forward(
                state
            )

            if decision > 0.5:
                agent.dino.jump()

        agent.dino.update()

        agent.fitness += 1

        for obs in game.obstacles:

            if agent.dino.get_rect().colliderect(
                obs.get_rect()
            ):
                agent.alive = False
                break

    game.draw(screen)

    alive_count = 0

    for agent in agents:

        if agent.alive:

            alive_count += 1

            agent.dino.draw(screen)

    alive_text = font.render(
        f"Alive: {alive_count}",
        True,
        BLACK
    )

    generation_text = font.render(
        f"Generation: {generation}",
        True,
        BLACK
    )

    screen.blit(
        alive_text,
        (20, 60)
    )

    screen.blit(
        generation_text,
        (20, 100)
    )

    pygame.display.flip()

    if alive_count == 0:

        print(
            f"\nGeneration {generation} finished"
        )

        agents = next_generation(
            agents
        )

        generation += 1

        game = Game()

pygame.quit()