from Fitness import Fitness
from Individual import Individual
import numpy as np


class Population:

    def __init__(self, population_amount, pcb):
        self.__population_amount = population_amount
        self.__pcb = pcb
        individuals_list = []
        for x in range(population_amount):
            individuals_list.append(Individual(pcb))
        self.__individuals = individuals_list

    @property
    def population_amount(self):
        return self.__population_amount

    @population_amount.setter
    def population_amount(self, population_amount):
        self.__population_amount = population_amount

    @property
    def pcb(self):
        return self.__pcb

    @pcb.setter
    def pcb(self, pcb):
        self.__pcb = pcb

    @property
    def individuals(self):
        return self.__individuals

    @individuals.setter
    def individuals(self, individuals_list):
        self.__individuals = individuals_list

    def best_and_avergae_fitness_in_population(self):
        fitness = []
        for ind in self.individuals:
            fit = Fitness(ind)
            fitness.append(fit.count_fitness())
        print("AVERAGE: " + str(np.average(fitness)))

        return self.individuals[min(range(len(fitness)), key=fitness.__getitem__)]