from Generator import Generator
from PCB import PCB
from PCBPrinter import PCBPrinter
from Population import Population
import Operators as op


def evaluate_population(population, n, selection):
    best_fitness = population.best_worst_fitness_in_population()[0]
    best_ind = population.best_worst_fitness_in_population()[2]
    for x in range(n):
        print(x)
        new_population = Population(0, population.pcb)

        # until ne population amount = previous one
        while new_population.population_amount < population.population_amount:
            if selection == "tournament":
                parent_1 = op.selection_tournament(population)
                parent_2 = op.selection_tournament(population)
            elif selection == "roulette":
                parent_1 = op.selection_roulette(population)
                parent_2 = op.selection_roulette(population)
            # if there is place for only one individual, get random parent
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
                    # there is no crossing, get random parent
                    new_population.population_amount += 1
                    children = op.mutation(children, True)
                    new_population.individuals.append(children)

        new_best, _, new_ind, _ = new_population.best_worst_fitness_in_population()
        if new_best < best_fitness:
            best_fitness = new_best
            best_ind = new_ind


        #p.draw_plot(new_population.best_worst_and_avergae_fitness_in_population()[2])
        population = new_population
        #if x == n-1:
        p = PCBPrinter(new_population)
        p.draw_plot(best_ind)

    return best_fitness


if __name__ == '__main__':

    # BOARD
    pcb = PCB()
    pcb.read_from_file("Zadania/zad2.txt")
    print(pcb)
    print("---------------------")

    # GENERATE POPULATION
    pop = Population(200, pcb)

    fitness = []
    for ind in pop.individuals:
        gen = Generator(ind)
        gen.generate_random_paths()
        #ind.print_paths()

    #     fit = Fitness(pop.individuals[x])
    #     fitness.append(fit.count_fitness())
    #
    # print("BEST OF ALL:", str(min(fitness)))
    # print("WORST OF ALL:", str(max(fitness)))
    # print("AVERAGE:", str(np.average(fitness)))
    # print("STANDARD DEVIATION:", str(np.std(fitness)))

    printer = PCBPrinter(pop)
    printer.draw_plot(pop.best_worst_fitness_in_population()[2])
    evaluate_population(pop, 100, "tournament")

    # genetic algorithm x times
    # best_individuals = []
    #
    # for x in range(10):
    #     print("POPULATION:", x)
    #     best = evaluate_population(pop, 19, "tournament")
    #     print("BEST:", str(best))
    #     best_individuals.append(best)
    #
    # print("BEST OF ALL:", str(min(best_individuals)))
    # print("WORST OF ALL:", str(max(best_individuals)))
    # print("AVERAGE:", str(np.average(best_individuals)))
    # print("STANDARD DEVIATION:", str(np.std(best_individuals)))
