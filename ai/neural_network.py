import numpy as np


class NeuralNetwork:

    def __init__(self):

        self.W1 = np.random.randn(6, 8)
        self.W2 = np.random.randn(8, 8)
        self.W3 = np.random.randn(8, 1)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, x):

        x = np.array(x)

        h1 = np.tanh(x @ self.W1)

        h2 = np.tanh(h1 @ self.W2)

        out = self.sigmoid(h2 @ self.W3)

        return out[0]

    def copy(self):

        child = NeuralNetwork()

        child.W1 = self.W1.copy()
        child.W2 = self.W2.copy()
        child.W3 = self.W3.copy()

        return child

    def mutate(self, mutation_rate=0.1):

        for matrix in [self.W1, self.W2, self.W3]:

            mask = np.random.rand(*matrix.shape) < mutation_rate

            matrix += mask * np.random.normal(
                0,
                0.5,
                matrix.shape
            )