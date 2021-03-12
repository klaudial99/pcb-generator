class Fitness:

    def __init__(self, individual):
        segments_amount = 0
        full_length = 0

        for path in individual.paths:
            segments_amount += len(path.segments)
            full_length += len(path.visited_points)
        full_length -= len(individual.paths)

        self.__individual = individual
        self.__segments_amount = segments_amount
        self.__full_length = full_length
        self.__crosses = 0

    @property
    def individual(self):
        return self.__individual

    @individual.setter
    def individual(self, individual):
        self.__individual = individual

    @property
    def segments_amount(self):
        return self.__segments_amount

    @segments_amount.setter
    def segments_amount(self, segments_amount):
        self.__segments_amount = segments_amount

    @property
    def full_length(self):
        return self.__full_length

    @full_length.setter
    def full_length(self, full_length):
        self.__full_length = full_length

    @property
    def crosses(self):
        return self.__crosses

    @crosses.setter
    def crosses(self, crosses):
        self.__crosses = crosses

    def count_crosses(self):
        points_dict = {}
        for path in self.individual.paths:
            for point in path.visited_points:
                if str(point) in points_dict.keys():
                    points_dict[str(point)] = points_dict[str(point)] + 1
                else:
                    points_dict[str(point)] = 1

        counter = 0
        for key, value in points_dict.items():
            if value > 1:
                counter += value-1

        self.crosses = counter

    def count_fitness(self, length_weight=2, segments_weight=1, cross_weight=5):
        return self.segments_amount*segments_weight + self.full_length*length_weight + self.crosses*cross_weight

    def get_info(self):
        return [self.full_length, self.segments_amount, self.crosses]
