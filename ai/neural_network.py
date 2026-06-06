import numpy as np

class NeuralNetwork:

    def __init__(self):

        self.W1 = np.random.randn(6, 8)
        self.W2 = np.random.randn(8, 8)
        self.W3 = np.random.randn(8, 1)

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))
    
    def forward(self, x):

        x = np.array(x)

        h1 = np.tanh(x @ self.W1)

        h2 = np.tanh(h1 @ self.W2)

        out = self.sigmoid(h2 @ self.W3)

        return out[0]