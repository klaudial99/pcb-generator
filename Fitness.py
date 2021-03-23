import AlgorithmParameters as ap
from Point import Point


def increase_visits(point, dictionary):
    if str(point) in dictionary.keys():
        dictionary[str(point)] = dictionary[str(point)] + 1
    else:
        dictionary[str(point)] = 1


def point_out_of_board(point, pcb):
    height = pcb.height
    width = pcb.width

    if point.x > width or point.x < 0 or point.y > height or point.y < 0:
        return True
    else:
        return False


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
        self.__paths_out_of_board = 0
        self.__length_out_of_board = 0
        self.count_out_of_board()
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

    @property
    def paths_out_of_board(self):
        return self.__paths_out_of_board

    @paths_out_of_board.setter
    def paths_out_of_board(self, paths_out_of_board):
        self.__paths_out_of_board = paths_out_of_board

    @property
    def length_out_of_board(self):
        return self.__length_out_of_board

    @length_out_of_board.setter
    def length_out_of_board(self, length_out_of_board):
        self.__length_out_of_board = length_out_of_board

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

    def count_out_of_board(self):
        #paths
        for path in self.individual.paths:
            for seg in path.segments:
                if point_out_of_board(seg.start_point, self.individual.pcb) or point_out_of_board(seg.end_point, self.individual.pcb):
                    self.paths_out_of_board += 1
                    break
        #length
        for path in self.individual.paths:
            for seg in path.segments:

                if point_out_of_board(seg.start_point, self.individual.pcb) and point_out_of_board(seg.end_point, self.individual.pcb):
                    self.length_out_of_board += seg.length

                elif point_out_of_board(seg.start_point, self.individual.pcb) or point_out_of_board(seg.end_point, self.individual.pcb):
                    counter = 0
                    if seg.length == 1:
                        counter += 1
                    else:
                        if point_out_of_board(seg.start_point, self.individual.pcb):
                            counter += 1
                        prev_point = seg.start_point

                        for x in range(seg.length):
                            if seg.direction == 1:
                                p = Point(prev_point.x, prev_point.y + 1)
                            elif seg.direction == 2:
                                p = Point(prev_point.x + 1, prev_point.y)
                            elif seg.direction == 3:
                                p = Point(prev_point.x, prev_point.y - 1)
                            elif seg.direction == 4:
                                p = Point(prev_point.x - 1, prev_point.y)

                            if point_out_of_board(p, self.individual.pcb):
                                counter += 1
                            prev_point = p

                    self.length_out_of_board += counter

    def count_fitness(self):
        return self.segments_amount*ap.SEGMENTS_WEIGHT + self.full_length*ap.LENGTH_WEIGHT + self.crosses*ap.CROSS_WEIGHT \
               + self.paths_out_of_board*ap.PATH_OUT_OF_BOARD + self.length_out_of_board*ap.LENGTH_OUT_OF_BOARD

    def get_info(self):
        return [self.full_length, self.segments_amount, self.crosses, self.paths_out_of_board, self.length_out_of_board]
