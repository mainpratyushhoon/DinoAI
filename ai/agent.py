from dino import Dino
from ai.neural_network import NeuralNetwork


class Agent:

    def __init__(self, brain=None):

        self.dino = Dino()

        if brain is None:
            self.brain = NeuralNetwork()
        else:
            self.brain = brain

        self.alive = True

        self.fitness = 0