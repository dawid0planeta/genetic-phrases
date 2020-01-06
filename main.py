import string
import random
from Population import *
from DNA import *

POP_SIZE = 500 
MUTATION_RATE = 0.01
GOAL = 'To be or not to be.'

# create first population
population = Population(POP_SIZE, GOAL, MUTATION_RATE, rand=True)

while True:
    population.calculate_fitness()
    population.generate_mating_pool()
    population.natural_selection()
    if population.best_member.genome == GOAL:
        print('Done')
        break







