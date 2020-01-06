import random
import string


def random_letter():
    return random.choice(string.digits + string.punctuation + string.ascii_letters + ' ')


class DNA():
    def __init__(self, goal, mutation_rate, rand=False):
        self.goal = goal
        self.size = len(goal)
        self.genome = ''
        self.fitness = 0
        self.mutation_rate = mutation_rate
        if rand:
            for gene in range(self.size):
                self.genome += random_letter()

    def calculate_fitness(self):
        fit = 0
        for i in range(self.size):
            if self.genome[i] == self.goal[i]:
                fit += 1
        self.fitness = fit**2

    def mate(self, second_parent):
        divider = random.randint(0, self.size)
        child = DNA(self.goal, self.mutation_rate)
        child.genome = self.genome[:divider] + second_parent.genome[divider:]
        return child

    def mutate(self):
        genome_list = list(self.genome)
        for index in range(len(self.genome)):
            ran = random.uniform(0, 1)
            if ran < self.mutation_rate:
                genome_list[index] = random_letter()
        self.genome = ''.join(genome_list)

    def show(self):
        print(self.genome)
