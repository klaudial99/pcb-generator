import pickle
import random
from Fitness import Fitness
import AlgorithmParameters as ap
from Individual import Individual


# returns best from randomly chosen N individuals
def selection_tournament(population):
    selected_individuals = []
    selected_indexes = []

    # take all individuals if population is too small
    if ap.TOURNAMENT_N*len(population.individuals) >= len(population.individuals):
        selected_individuals = population.individuals
    else:
        while len(selected_individuals) < ap.TOURNAMENT_N*len(population.individuals):

            # get random index which wasn't used
            while True:
                random_index = random.randint(0, len(population.individuals) - 1)
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
    #print("Tournament - selected fitness:", fit.count_fitness())

    return selected_individuals[index_min]


# returns randomly chosen individual - each has other odds to be chosen
def selection_roulette(population):
    # weight/100 for each individual
    weights = []
    for ind in population.individuals:
        fit = Fitness(ind)
        weights.append(1 / fit.count_fitness())

    weights_sum = sum(weights)

    # odds for being chosen, oddds = weight/sum
    odds = []
    for x in range(len(population.individuals)):
        odds.append(weights[x] / weights_sum)

    random_number = random.random()

    # finding individual related to random number
    roulette_sum = 0
    #print("SUM", sum(odds))
    for x in range(len(odds)):
        roulette_sum += odds[x]
        #print("sum", roulette_sum)
        if random_number <= roulette_sum:
            #print("random", random_number)
            fit = Fitness(population.individuals[x])
            #print("Roulette - selected fitness:", fit.count_fitness())
            return population.individuals[x]


def return_random_parent(ind1, ind2):
    random_parent = random.randint(1, 2)
    if random_parent == 1:
        return ind1
    else:
        return ind2


def crossover(ind1, ind2):
    crossing_odds = random.randint(0, 100)
    # return references to one of parents if not crossing
    if crossing_odds > ap.CROSSING_PROBABILITY:
        parent = return_random_parent(ind1, ind2)
        return parent
    # if crossing
    else:
        paths_child_1 = []
        paths_child_2 = []
        for x in range(len(ind1.paths)):
            gene_change_odds = random.randint(0, 100)
            # swap genes, deep copy - to avoid changing the parent
            if gene_change_odds < ap.GENE_CHANGE_PROBABILITY:
                paths_child_1.append(pickle.loads(pickle.dumps(ind2.paths[x])))
                paths_child_2.append(pickle.loads(pickle.dumps(ind1.paths[x])))
            # else original genes
            else:
                paths_child_1.append(pickle.loads(pickle.dumps(ind1.paths[x])))
                paths_child_2.append(pickle.loads(pickle.dumps(ind2.paths[x])))

        # new children
        child_1 = Individual(ind1.pcb)
        child_1.paths = paths_child_1

        child_2 = Individual(ind1.pcb)
        child_2.paths = paths_child_2

        return child_1, child_2


def mutation(individual, is_ref):
    # copy if ind is a referencw
    if is_ref:
        ind = pickle.loads(pickle.dumps(individual))

    else:
        ind = individual
    for path in ind.paths:
        if len(path.segments) > 1:
            mutation_odds = random.randint(0, 100)
            if mutation_odds < ap.MUTATION_PROBABILITY:
                # get random segment for mutation
                segment = random.randint(0, len(path.segments) - 2)
                # if longer than 1, draw lengthening or shortening
                if path.segments[segment].length > 1:
                    operation = random.randint(0, 1)  # 0 = shortening, 1 = lengthening
                else:
                    operation = 1

                if operation == 1:
                    path.lengthening_segment(segment)
                    ind.check_paths()

                else:
                    path.shortening_segment(segment)
                    ind.check_paths()
    return ind
