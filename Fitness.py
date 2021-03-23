import AlgorithmParameters as ap
from Point import Point


def increase_visits(point, dictionary):
    if str(point) in dictionary.keys():
        dictionary[str(point)] = dictionary[str(point)] + 1
    else:
        dictionary[str(point)] = 1


class Fitness:

    def __init__(self, individual):
        segments_amount = 0
        full_length = 0

        for path in individual.paths:
            segments_amount += len(path.segments)
            for seg in path.segments:
                full_length += seg.length

        self.__individual = individual
        self.__segments_amount = segments_amount
        self.__full_length = full_length
        self.__crosses = 0
        self.count_crosses()

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
            for seg in path.segments:
                increase_visits(seg.start_point, points_dict)
                if seg.length > 1:
                    last_point = seg.start_point
                    for x in range(seg.length-1):

                        if seg.direction == 1:
                            p = Point(last_point.x, last_point.y+1)
                            increase_visits(p, points_dict)
                            last_point = p
                        elif seg.direction == 2:
                            p = Point(last_point.x+1, last_point.y)
                            increase_visits(p, points_dict)
                            last_point = p
                        elif seg.direction == 3:
                            p = Point(last_point.x, last_point.y-1)
                            increase_visits(p, points_dict)
                            last_point = p
                        elif seg.direction == 4:
                            p = Point(last_point.x-1, last_point.y)
                            increase_visits(p, points_dict)
                            last_point = p
            increase_visits(path.link.end_point, points_dict)

        counter = 0
        for key, value in points_dict.items():
            if value > 1:
                counter += value-1

        self.crosses = counter

    def count_fitness(self):
        return self.segments_amount*ap.SEGMENTS_WEIGHT + self.full_length*ap.LENGTH_WEIGHT + self.crosses*ap.CROSS_WEIGHT

    def get_info(self):
        return [self.full_length, self.segments_amount, self.crosses]
