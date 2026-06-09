import pygame
import random
from settings import *
from game import Game
from ai.agent import Agent
generation_scores = []
def select_parent(population):

    tournament = random.sample(
        population,
        5
    )

    return max(
        tournament,
        key=lambda a: a.fitness
    )
def next_generation(old_agents):

    old_agents.sort(
        key=lambda a: a.fitness,
        reverse=True
    )

    best = old_agents[0]

    generation_scores.append(
        best.fitness
    )

    print(
        f"Best fitness: {best.fitness}"
    )

    new_agents = []

    ELITES = 5

    for i in range(ELITES):

        new_agents.append(
            Agent(
                old_agents[i].brain.copy()
            )
        )

    parents = old_agents[:20]

    while len(new_agents) < len(old_agents):

        parent1 = select_parent(
            parents
        )

        parent2 = select_parent(
            parents
        )

        child_brain = (
            parent1.brain.crossover(
                parent2.brain
            )
        )

        child_brain.mutate(
            mutation_rate=0.1
        )

        new_agents.append(
            Agent(
                child_brain
            )
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

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.plot(
    range(1, len(generation_scores) + 1),
    generation_scores
)

plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Dino AI Learning Curve")

plt.grid(True)

plt.show()