from Point import Point


class Segment:

    def __init__(self, start_point, direction, end_point=None, length=0):
        if end_point is None:
            end_point = start_point
        self.__start_point = start_point
        self.__end_point = end_point
        self.__direction = direction
        self.__length = length

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

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    def set_end_point(self, point):
        if isinstance(point, Point):
            self.end_point = point

    def __repr__(self):
        return str(self.start_point) + " " + str(self.direction) + " " + str(self.length)

