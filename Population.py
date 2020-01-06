from DNA import *


def translate(old_value, old_min, old_max, new_min, new_max):
    old_range = (old_max - old_min)
    if (old_range == 0):
        return new_min
    else:
        new_range = (new_max - new_min)
        return (((old_value - old_min) * new_range) / old_range) + new_min


class Population():
    def __init__(self, pop_size, goal, mutation_rate, rand=False):
        self.goal = goal
        self.pop_size = pop_size
        self.members = []
        self.mating_pool = []
        self.mutation_rate = mutation_rate
        if rand:
            for index in range(self.pop_size):
                member = DNA(self.goal, self.mutation_rate, rand=True)
                self.members.append(member)

    def calculate_fitness(self):
        self.best_fit = 0
        for member in self.members:
            member.calculate_fitness()
            if self.best_fit < member.fitness:
                self.best_fit = member.fitness
                self.best_member = member

    def generate_mating_pool(self):
        self.mating_pool = [self.best_member]
        for each in self.members:
            instances = int(
                100 * translate(each.fitness, 0, self.best_fit, 0, 1))
            for i in range(instances):
                self.mating_pool.append(each)

    def natural_selection(self):
        self.best_member.show()
        self.members = []
        for i in range(self.pop_size):
            parent_a = random.choice(self.mating_pool)
            parent_b = random.choice(self.mating_pool)
            child = parent_a.mate(parent_b)
            child.mutate()
            self.members.append(child)

    def show(self):
        for member in self.members:
            member.show()
