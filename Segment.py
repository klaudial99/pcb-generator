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

    def lengthen_segment(self):
        # determine new end point
        if self.direction == 1:
            #self.end_point.y += 1
            self.end_point = Point(self.end_point.x, self.end_point.y+1)
        elif self.direction == 2:
            #self.end_point.x += 1
            self.end_point = Point(self.end_point.x+1, self.end_point.y)
        elif self.direction == 3:
            #self.end_point.y -= 1
            self.end_point = Point(self.end_point.x, self.end_point.y - 1)
        elif self.direction == 4:
            #self.end_point.x -= 1
            self.end_point = Point(self.end_point.x-1, self.end_point.y)
        self.length += 1


    def shorten_segment(self):
        # determine new end point
        if self.direction == 1:
            self.end_point = Point(self.end_point.x, self.end_point.y - 1)
        elif self.direction == 2:
            self.end_point = Point(self.end_point.x-1, self.end_point.y)
        elif self.direction == 3:
            self.end_point = Point(self.end_point.x, self.end_point.y + 1)
        elif self.direction == 4:
            self.end_point = Point(self.end_point.x+1, self.end_point.y)

        self.length -= 1

    def lengthen_segment_back(self):
        # determine new start point
        if self.direction == 1:
            self.start_point = Point(self.start_point.x, self.start_point.y - 1)
        elif self.direction == 2:
            self.start_point = Point(self.start_point.x-1, self.start_point.y)
        elif self.direction == 3:
            self.start_point = Point(self.start_point.x, self.start_point.y + 1)
        elif self.direction == 4:
            self.start_point = Point(self.start_point.x+1, self.start_point.y)

        self.length += 1

    def shorten_segment_back(self):
        # determine new start point
        if self.direction == 1:
            self.start_point = Point(self.start_point.x, self.start_point.y + 1)
        elif self.direction == 2:
            self.start_point = Point(self.start_point.x+1, self.start_point.y)
        elif self.direction == 3:
            self.start_point = Point(self.start_point.x, self.start_point.y - 1)
        elif self.direction == 4:
            self.start_point = Point(self.start_point.x-1, self.start_point.y)

        self.length -= 1

    def move_segment_lengthening(self, prev_segment):
        # determine direction of moving
        if prev_segment.direction == 1:
            self.start_point = Point(self.start_point.x, self.start_point.y+1)
            self.end_point = Point(self.end_point.x, self.end_point.y+1)
        elif prev_segment.direction == 2:
            self.start_point = Point(self.start_point.x+1, self.start_point.y)
            self.end_point = Point(self.end_point.x+1, self.end_point.y)
        elif prev_segment.direction == 3:
            self.start_point = Point(self.start_point.x, self.start_point.y-1)
            self.end_point = Point(self.end_point.x, self.end_point.y-1)
        elif prev_segment.direction == 4:
            self.start_point = Point(self.start_point.x-1, self.start_point.y)
            self.end_point = Point(self.end_point.x-1, self.end_point.y)

    def move_segment_shortening(self, prev_segment):
        # determine direction of moving
        if prev_segment.direction == 1:
            self.start_point = Point(self.start_point.x, self.start_point.y - 1)
            self.end_point = Point(self.end_point.x, self.end_point.y - 1)
        elif prev_segment.direction == 2:
            self.start_point = Point(self.start_point.x - 1, self.start_point.y)
            self.end_point = Point(self.end_point.x - 1, self.end_point.y)
        elif prev_segment.direction == 3:
            self.start_point = Point(self.start_point.x, self.start_point.y + 1)
            self.end_point = Point(self.end_point.x, self.end_point.y + 1)
        elif prev_segment.direction == 4:
            self.start_point = Point(self.start_point.x + 1, self.start_point.y)
            self.end_point = Point(self.end_point.x + 1, self.end_point.y)

    def __repr__(self):
        return str(self.start_point) + " " + str(self.direction) + " " + str(self.length)

