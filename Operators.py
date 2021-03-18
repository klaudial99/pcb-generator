import random

from Fitness import Fitness


# returns best from randomly chosen N individuals
def selection_tournament(population, tournament_N):
    selected_individuals = []
    selected_indexes = []

    # take all individuals if population is too small
    if tournament_N >= len(population.individuals):
        selected_individuals = population.individuals
    else:
        while len(selected_individuals) < tournament_N:

            # get random index which wasn't used
            while True:
                random_index = random.randint(0, len(population.individuals)-1)
                if random_index not in selected_indexes:
                    break

            # add reference to chosen individual and it's index
            selected_individuals.append(population.individuals[random_index])
            selected_indexes.append(random_index)

    # fitness for every individual
    fitness = []
    for ind in selected_individuals:
        fit = Fitness(ind)
        fitness.append(fit.count_fitness())

    # get index of smallest fitness
    index_min = min(range(len(fitness)), key=fitness.__getitem__)
    fit = Fitness(selected_individuals[index_min])
    print("Tournament - selected fitness:", fit.count_fitness())

    return selected_individuals[index_min]


# returns randomly chosen individual - each has other odds to be chosen
def selection_roulette(population):
    # weight/100 for each individual
    weights = []
    for ind in population.individuals:
        fit = Fitness(ind)
        weights.append(fit.count_fitness()/100)

    weights_sum = sum(weights)

    # odds for being chosen, oddds = weight/sum
    odds = []
    for x in range(len(population.individuals)):
        odds.append(weights[x]/weights_sum)

    random_number = random.random()

    # finding individual related to random number
    roulette_sum = 0
    for x in range(len(odds)):
        roulette_sum += odds[x]
        if random_number <= roulette_sum:
            fit = Fitness(population.individuals[x])
            print("Roulette - selected fitness:", fit.count_fitness())
            return population.individuals[x]
