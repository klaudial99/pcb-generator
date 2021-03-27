from Path import Path
from Segment import Segment


class Individual:

    def __init__(self, pcb):

        self.__pcb = pcb
        self.__paths = []

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

    def check_paths(self):
        for path in self.paths:
            for i in range(len(path.segments)-1):
                if path.segments[i].end_point != path.segments[i+1].start_point:
                    print(path)
                    raise Exception("END, START")
                if path.segments[i].start_point == path.segments[i].end_point:
                    print(path)
                    raise Exception("SAME POINT")
            if path.segments[-1].start_point == path.segments[-1].end_point:
                print(path)
                raise Exception("LAST SAME")

    def __repr__(self):
        return "PCB: " + str(self.pcb) + "\n" + str(self.paths)
