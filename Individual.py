from Path import Path
from Segment import Segment


class Individual:

    def __init__(self, pcb):

        self.__pcb = pcb
        self.__paths = []
        self.__crosses = 0

        self.create_paths()

    @property
    def pcb(self):
        return self.__pcb

    @pcb.setter
    def pcb(self, pcb):
        self.__pcb = pcb

    @property
    def paths(self):
        return self.__paths

    @paths.setter
    def paths(self, paths):
        self.__paths = paths

    @property
    def crosses(self):
        return self.__crosses

    @crosses.setter
    def crosses(self, crosses):
        self.__crosses = crosses

    # creates paths with first segments
    def create_paths(self):
        links = self.pcb.board_links
        paths_from_links = []
        for link in links:
            paths_from_links.append(Path(link, [Segment(link.start_point, 0)]))
        self.paths = paths_from_links

    def print_paths(self):
        for path in self.paths:
            print(path)

    # counts points with more than one visit
    def count_crosses(self):
        points_dict = {}
        for path in self.paths:
            for point in path.visited_points:
                if str(point) in points_dict.keys():
                    points_dict[str(point)] = points_dict[str(point)] + 1
                else:
                    points_dict[str(point)] = 1

        counter = 0
        for key, value in points_dict.items():
            if value > 1:
                counter += 1

        self.crosses = counter

    def count_fitness(self):
        segments_amount = 0
        full_length = 0
        for path in self.paths:
            segments_amount += len(path.segments)
            full_length += len(path.visited_points)

        full_length -= len(self.paths)

        #print(segments_amount)
        #print(full_length)

        return self.crosses*5 + segments_amount + full_length*2

    def __repr__(self):
        return "PCB: " + str(self.pcb) + "\n" + str(self.paths)



