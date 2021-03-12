from Point import Point


class Path:

    def __init__(self, link_object, segments_objects_list=None):
        if segments_objects_list is None:
            segments_objects_list = []
        self.__link = link_object
        self.__segments = segments_objects_list
        self.__visited_points = [link_object.start_point]

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, link_object):
        self.__link = link_object

    @property
    def segments(self):
        return self.__segments

    @property
    def visited_points(self):
        return self.__visited_points

    @visited_points.setter
    def visited_points(self, visited_points):
        self.__visited_points = visited_points

    def add_visited_point(self, point):
        if isinstance(point, Point):
            self.visited_points.append(point)

    def set_last_segment(self, segment):
        self.segments[-1] = segment

    def add_segment(self, segment):
        self.segments.append(segment)

    def __repr__(self):
        return_string = "LINK: " + str(self.link) + "\n"
        for seg in self.segments:
            return_string += "SEGMENT: " + str(seg) + "\n"
        return return_string
