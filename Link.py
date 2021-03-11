class Link:

    def __init__(self, start_point, end_point):
        self.__start_point = start_point
        self.__end_point = end_point

    @property
    def start_point(self):
        return self.__start_point

    @start_point.setter
    def start_point(self, start_point):
        self.__start_point = start_point

    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    def end_point(self, end_point):
        self.__end_point = end_point

    def __eq__(self, other):
        if isinstance(other, Link):
            return (self.start_point == other.start_point and self.end_point == other.end_point) or \
                   (self.start_point == other.end_point and self.end_point == other.start_point)
        else:
            return False

    def __repr__(self):
        return str(self.start_point) + " - " + str(self.end_point)