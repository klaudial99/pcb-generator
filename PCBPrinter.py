import random

import matplotlib.pyplot as plt
import numpy as np

from Fitness import Fitness
from Generator import Generator
from PCB import PCB
from Population import Population


class PCBPrinter:

    def __init__(self, population):
        self.__population = population
        self.__pcb = population.individuals[0].pcb

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        self.__population = population

    @property
    def pcb(self):
        return self.__pcb

    @pcb.setter
    def pcb(self, pcb):
        self.__pcb = pcb

    def draw_plot(self, best_individual, ind_info, fitness):

        # FRAME
        x_frame = np.array([0, 0, self.pcb.width, self.pcb.width, 0])
        y_frame = np.array([0, self.pcb.height, self.pcb.height, 0, 0])
        plt.plot(x_frame, y_frame)

        # TITLE
        title_font = {'family': 'serif', 'size': 16}
        plt.title("BEST INDIVIDUAL: " + str(best_individual + 1), fontdict=title_font)

        for path in self.population.individuals[best_individual].paths:

            rand_color = "#%06x" % random.randint(0, 0xFFFFFF)

            # START & END POINT
            start = path.link.start_point
            end = path.link.end_point
            plt.plot([start.x], [start.y], marker='o', color=rand_color, ms=10)
            plt.plot([end.x], [end.y], marker='x', color=rand_color, ms=10)

            # SEGMENTS
            x_segments = [path.segments[0].start_point.x]
            y_segments = [path.segments[0].start_point.y]

            for segment in path.segments:
                x_segments.append(segment.end_point.x)
                y_segments.append(segment.end_point.y)

            plt.plot(x_segments, y_segments, color=rand_color)

        plt.figtext(0.5, 0.01, 'Length: ' + str(ind_info[best_individual][0]) + '   Segments: '
                    + str(ind_info[best_individual][1]) + '   Crosses: ' + str(ind_info[best_individual][2])
                    + '   Fitness: ' + str(fitness[best_individual]), ha='center')
        plt.grid()
        plt.show()


if __name__ == '__main__':

    # BOARD
    pcb = PCB()
    pcb.read_from_file("D:/studia/6. sem/Sztuczna inteligencja i inżynieria wiedzy/Laborki/lista1/zad0.txt")
    print(pcb)
    print("---------------------")

    # GENERATE POPULATION
    pop = Population(3, pcb)

    for ind in pop.individuals:
        gen = Generator(ind)
        gen.generate_random_paths()
        #ind.print_paths()

    # CHECK POPULATION FITNESS
    fitness = []
    individual_info = {}
    for x in range(len(pop.individuals)):
        fit = Fitness(pop.individuals[x])
        fit.count_crosses()
        individual_info[x] = fit.get_info()
        fitness.append(fit.count_fitness())

    index_best = min(range(len(fitness)), key=fitness.__getitem__)

    for x in range(len(fitness)):
        print("INDIVIDUAL " + str(x + 1) + ": " + str(fitness[x]))

    print("AVERAGE: " + str(np.average(fitness)))

    # MATLIBPLOT
    printer = PCBPrinter(pop)
    printer.draw_plot(index_best, individual_info, fitness)
