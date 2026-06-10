# 🦖 DinoAI

A Genetic Algorithm + Neural Network powered AI that learns to play a custom implementation of the Chrome Dino game through neuroevolution.

This project implements a complete evolutionary learning pipeline from scratch without using machine learning frameworks such as TensorFlow, PyTorch, Stable Baselines, or NEAT. Neural networks, mutation, crossover, selection, and fitness evaluation are implemented manually using NumPy.

---

## Features

* Custom Chrome Dino game built with Pygame
* Multiple obstacle types

  * Small Cactus
  * Tall Cactus
  * Double Cactus
* Dynamic difficulty scaling
* Double jump mechanics
* Feedforward neural network controller
* Population-based training
* Tournament selection
* Genetic crossover
* Mutation-based exploration
* Elite preservation
* Fitness tracking
* Generation-wise learning statistics
* Training curve visualization

---

## Project Structure

```text
DinoAI/
│
├── assets/
│   ├── dino.png
│   ├── smallcactus.png
│   ├── tallcactus.png
│   └── twocactus.png
│
├── ai/
│   ├── agent.py
│   └── neural_network.py
│
├── dino.py
├── obstacle.py
├── game.py
├── settings.py
├── main.py
└── README.md
```

---

## Architecture Overview

```text
Game Environment
        ↓
Neural Network Controller
        ↓
Genetic Algorithm Optimizer
```

---

## Environment

The environment is a custom recreation of the Chrome Dino game.

### State Representation

Each agent receives a normalized observation vector:

```text
Obstacle 1 Distance
Obstacle 1 Width
Obstacle 1 Height

Obstacle 2 Distance
Obstacle 2 Width
Obstacle 2 Height

Game Speed

Dino Y Position
Dino Vertical Velocity

Remaining Jump State
```

These values are normalized before being fed into the neural network.

---

## Neural Network

The controller is a fully connected feedforward neural network.

### Architecture

```text
Input Layer
10 Neurons

↓

Hidden Layer 1
16 Neurons
tanh activation

↓

Hidden Layer 2
16 Neurons
tanh activation

↓

Output Layer
1 Neuron
sigmoid activation
```

### Output Interpretation

```python
if output > 0.5:
    jump()
```

---

## Neuroevolution

The project uses a Genetic Algorithm instead of gradient descent.

No labelled dataset is required.

No backpropagation is performed.

Learning occurs through:

```text
Random Initialization
        ↓
Evaluation
        ↓
Selection
        ↓
Crossover
        ↓
Mutation
        ↓
New Generation
```

---

## Population

```python
POPULATION_SIZE = 100
```

Each agent contains:

```text
Agent
├── Dino
├── Neural Network
├── Fitness
└── Alive State
```

---

## Fitness Function

Fitness is proportional to survival time.

```python
fitness += 1
```

per frame survived.

Agents that survive longer obtain higher fitness values and have a greater probability of contributing genetic material to the next generation.

---

## Selection

Tournament Selection is used.

A random subset of agents is sampled.

```python
TOURNAMENT_SIZE = 5
```

The fittest individual in the tournament becomes a parent.

This approach maintains selective pressure while preserving population diversity.

---

## Elitism

Top-performing individuals are copied directly into the next generation.

```python
ELITES = 5
```

This prevents loss of high-quality solutions due to random mutation.

---

## Crossover

Uniform crossover is used.

For every weight:

```text
50% chance → Parent A
50% chance → Parent B
```

Example:

```text
Parent A Weight = 0.84
Parent B Weight = -0.32

Child Weight
→ randomly selected from either parent
```

This allows useful traits from different agents to combine.

---

## Mutation

After crossover, weights are mutated.

```python
weight += N(0, σ)
```

Typical values:

```python
mutation_rate = 0.05
sigma = 0.05
```

Mutation introduces genetic diversity and allows exploration of new behaviors.

---

## Learning Process

### Early Generations

```text
Random behavior
Frequent collisions
Low fitness
```

### Intermediate Generations

```text
Basic obstacle avoidance
Improved jump timing
Higher fitness
```

### Advanced Generations

```text
Consistent obstacle avoidance
Strategic double-jump usage
High survival times
```

---

## Training Metrics

The project tracks:

* Generation Number
* Best Fitness
* Alive Agents
* Training Curve

Example visualization:

```python
plt.plot(generation_scores)
```

---

## Why Genetic Algorithms?

Traditional gradient-based learning requires:

```text
Input
Label
Loss Function
```

The Dino game does not provide correct actions.

Instead, the agent learns directly from environmental feedback.

Genetic Algorithms naturally solve this problem by optimizing behavior through survival and reproduction.

---

## Technologies Used

* Python 3.11+
* Pygame
* NumPy
* Matplotlib

---

## Future Improvements

* Flying bird obstacles
* Duck mechanic
* RNN / LSTM controllers
* NEAT implementation
* Parallel evaluation
* Save / Load champion genomes
* Replay system
* Live training dashboard
* Speciation
* Adaptive mutation rates
* Multi-objective fitness

---

## Example Results

```text
Generation 1
Best Fitness: 644

Generation 36
Best Fitness: 1001

Generation 84
Best Fitness: 1143

Generation 99
Best Fitness: 1260
```

These results demonstrate successful evolutionary learning from purely random initial policies.

---

## Running the Project

```bash
git clone <repo-url>
cd DinoAI

pip install pygame numpy matplotlib

python main.py
```

---

## License

MIT License
