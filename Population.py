from Generator import Generator
from Individual import Individual
from PCB import PCB


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


if __name__ == '__main__':

    pcb = PCB()
    pcb.read_from_file("D:/studia/6. sem/Sztuczna inteligencja i inżynieria wiedzy/Laborki/lista1/zad0.txt")
    print(pcb)
    print("---------------------")

    pop = Population(10, pcb)
    for ind in pop.individuals:
        gen = Generator(ind)
        gen.generate_random_paths()
        ind.print_paths()
        ind.count_crosses()

    counter = 0
    for ind in pop.individuals:
        counter += 1
        print("INDIVIDUAL " + str(counter) + ": " + str(ind.count_fitness()))






