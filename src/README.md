# Symbolic Regression Project

The project was done together to Antonio Sirica, s326811.
## Overview
This project focuses on solving the Symbolic Regression problem using an evolutionary algorithm. Symbolic Regression aims to discover mathematical expressions that best fit a given dataset, providing insights into the relationships between input variables and output values.

The work was conducted collaboratively by Luca Ianniello and Antonio Sirica (s326811).

## Problem Description
Symbolic Regression is a machine learning task where the goal is to find a symbolic expression that models the relationship between input variables and output values. Given a dataset of input-output pairs, the objective is to discover a formula that accurately predicts outputs from inputs.

In this project, we worked with 8 datasets, each with varying numbers of input variables and output values. The challenge was to identify the formula that best represents the underlying data for each dataset.

## Implementation Details
The problem was tackled using a custom evolutionary algorithm.

### Data Representation
- **Tree Structure**: Used to represent formulas as binary trees.
- **Node Structure**: Each node contains:
  - Value (operator, variable, or constant)
  - Type (operator or variable)
  - Left and right children (for binary operations)

### Operators and Variables
- **Operators**: Addition, subtraction, multiplication, division, sine, cosine, and exponential.
- **Variables**: Represented as `x1`, `x2`, ..., `xn`, where `n` is the number of input variables.
- **Constants**: Randomly generated within a range of 0.5 to 5 to avoid issues with zero values.

### Algorithm Workflow
1. **Initialization**:
   - Generate an initial population of binary trees representing candidate formulas.
   - Trees are initialized randomly by combining operators and variables.

2. **Fitness Evaluation**:
   - The fitness of an individual is calculated as the mean squared error (MSE) between predicted and actual values in the dataset.

3. **Parent Selection**:
   - Tournament selection is used, where the top 5 individuals are considered.
   - Two parents are selected from this group to generate offspring.

4. **Crossover**:
   - A random subtree of one parent is exchanged with a random subtree of the other parent to create two children.
   - One child is chosen randomly for further processing.

5. **Mutation**:
   - Each child has a 50% chance of undergoing mutation.
   - Mutation replaces a random subtree with a newly generated random subtree to enhance diversity and avoid local optima.

6. **Offspring Handling**:
   - Mutated and non-mutated children are added to an offspring buffer.

7. **Population Update**:
   - Merge offspring and parent populations.
   - Perform elitism to retain the top 5% of individuals.
   - Select the remaining 95% using a roulette wheel mechanism based on fitness.
   - Remove duplicates during selection.

8. **Iteration**:
   - Repeat the process for a fixed number of generations (50).

9. **Final Solution**:
   - Retain the best individual as the symbolic expression that best fits the dataset.

## Key Features
- **Tree-Based Representation**: Efficiently models complex formulas.
- **Diverse Operators**: Includes basic arithmetic and trigonometric functions.
- **Evolutionary Techniques**: Utilizes crossover, mutation, and selection to evolve solutions.
- **Elitism and Diversity Maintenance**: Ensures high-quality solutions while avoiding stagnation.

