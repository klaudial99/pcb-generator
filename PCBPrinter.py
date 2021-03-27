import random

import matplotlib.pyplot as plt
import numpy as np

from Fitness import Fitness


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

    def draw_plot(self, individual):
        plt.clf()
        # FRAME
        x_frame = np.array([0, 0, self.pcb.width, self.pcb.width, 0])
        y_frame = np.array([0, self.pcb.height, self.pcb.height, 0, 0])
        plt.plot(x_frame, y_frame, linestyle='dashed')

        # TITLE
        title_font = {'family': 'serif', 'size': 16}
        plt.title("BEST INDIVIDUAL", fontdict=title_font)

        for path in individual.paths:

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

        fit = Fitness(individual)
        fitness = fit.count_fitness()
        ind_info = fit.get_info()

        plt.figtext(0.2, 0, 'Length: ' + str(ind_info[0]) + '   Segments: '
                    + str(ind_info[1]) + '   Crosses: ' + str(ind_info[2])
                    + '   Fitness: ' + str(fitness) + '\nPaths out of board: ' + str(ind_info[3]) + '   Length out of board: ' + str(ind_info[4]))

        plt.grid()
        plt.draw()
        plt.waitforbuttonpress(0)
