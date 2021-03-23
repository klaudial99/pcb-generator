from Fitness import Fitness
from Generator import Generator
from Individual import Individual
from PCB import PCB
from PCBPrinter import PCBPrinter
from Path import Path
from Point import Point
from Population import Population
import Operators as op
from Segment import Segment


def evaluate_population(population, n, selection):
    for x in range(n):
        print(x)
        new_population = Population(0, population.pcb)
        # do zapełnienia populacji
        while new_population.population_amount < population.population_amount:
            if selection == "tournament":
                parent_1 = op.selection_tournament(population)
                parent_2 = op.selection_tournament(population)
            elif selection == "roulette":
                parent_1 = op.selection_roulette(population)
                parent_2 = op.selection_roulette(population)
            # jak zostaje jedno wolne miejsce to dobieram niezmienionego
            if new_population.population_amount == population.population_amount - 1:
                parent = op.return_random_parent(parent_1, parent_2)
                new_population.population_amount += 1
                parent = op.mutation(parent, True)
                new_population.individuals.append(parent)
            else:
                children = op.crossover(parent_1, parent_2)
                if type(children) == tuple:
                    new_population.population_amount += 2
                    for child in children:
                        child = op.mutation(child, False)
                        new_population.individuals.append(child)
                    #new_population.individuals.extend(children)
                else:
                    #nei dojdzie do krzyżowania i przechodzi losowy rodzic
                    new_population.population_amount += 1
                    children = op.mutation(children, True)
                    new_population.individuals.append(children)

        p = PCBPrinter(new_population)

        p.draw_plot(new_population.best_and_avergae_fitness_in_population())
        population = new_population
        # if x == n-1:
        #     p.draw_plot(new_population.best_and_avergae_fitness_in_population())


if __name__ == '__main__':

    # BOARD
    pcb = PCB()
    pcb.read_from_file("Zadania/zad1.txt")
    print(pcb)
    print("---------------------")

    # mypop = Population(0, pcb)
    # #
    # myind1 = Individual(pcb)
    # path1a = [Segment(Point(1, 3), 1, Point(1, 5), 2), Segment(Point(1, 5), 2, Point(2, 5), 1), Segment(Point(2, 5), 3, Point(2, 4), 1), Segment(Point(2, 4), 2, Point(4, 4), 2), Segment(Point(4, 4), 1, Point(4, 5), 1), Segment(Point(4, 5), 2, Point(5, 5), 1), Segment(Point(5, 5), 3, Point(5, 3), 2)]
    # path1b = [Segment(Point(3, 1), 1, Point(3, 2), 1), Segment(Point(3, 2), 2, Point(4, 2), 1), Segment(Point(4, 2), 1, Point(4, 3), 1), Segment(Point(4, 3), 4, Point(3, 3), 1)]
    # myind1.paths[0] = Path(pcb.board_links[0], path1a)
    # myind1.paths[1] = Path(pcb.board_links[1], path1b)
    # new_ind = op.mutation(myind1, False)
    # print("PAST MUTATION")
    # mypop.individuals.append(new_ind)
    # #
    # # myind2 = Individual(pcb)
    # # path2a = [Segment(Point(1, 3), 3, Point(1, 0), 3), Segment(Point(1, 0), 4, Point(0, 0), 1), Segment(Point(0, 0), 1, Point(0, 4), 4), Segment(Point(0, 4), 2, Point(2, 4), 2), Segment(Point(2, 4), 3, Point(2, 2), 2), Segment(Point(2, 2), 2, Point(5, 2), 3), Segment(Point(5, 2), 1, Point(5, 3), 1)]
    # # path2b = [Segment(Point(3, 1), 3, Point(4, 1), 1), Segment(Point(4, 1), 1, Point(4, 4), 3), Segment(Point(4, 4), 4, Point(3, 4), 1), Segment(Point(3, 4), 3, Point(3, 3), 1)]
    # # myind2.paths[0] = Path(pcb.board_links[0], path2a)
    # # myind2.paths[1] = Path(pcb.board_links[1], path2b)
    # # mypop.individuals.append(myind2)
    # #
    # printer = PCBPrinter(mypop)
    # printer.draw_plot(mypop.best_and_avergae_fitness_in_population())
    #
    # op.mutation(myind, True)
    #
    # printer.draw_plot(mypop.best_and_avergae_fitness_in_population())

    # GENERATE POPULATION
    pop = Population(1000, pcb)

    for ind in pop.individuals:
        gen = Generator(ind)
        gen.generate_random_paths()
        #ind.print_paths()

    # for ind in pop.individuals:
    #     ind.check_paths()
    # # CHECK POPULATION FITNESS
    # fitness = []
    # individual_info = {}
    # for x in range(len(pop.individuals)):
    #     fit = Fitness(pop.individuals[x])
    #     individual_info[x] = fit.get_info()
    #     fitness.append(fit.count_fitness())
    #
    # index_best = min(range(len(fitness)), key=fitness.__getitem__)
    #
    # for x in range(len(fitness)):
    #     print("INDIVIDUAL " + str(x + 1) + ": " + str(fitness[x]))
    #
    # print("AVERAGE: " + str(np.average(fitness)))

    # MATLIBPLOT

    printer = PCBPrinter(pop)
    printer.draw_plot(pop.best_and_avergae_fitness_in_population())

    evaluate_population(pop, 50, "tournament")

