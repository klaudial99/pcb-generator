import copy

from Point import Point
from Segment import Segment


def get_opposite_direction(direction):
    if direction == 1:
        return 3
    elif direction == 2:
        return 4
    elif direction == 3:
        return 1
    elif direction == 4:
        return 2


class Path:

    def __init__(self, link_object, segments_objects_list=None):
        if segments_objects_list is None:
            segments_objects_list = []
        self.__link = link_object
        self.__segments = segments_objects_list

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

    def remove_segment(self, n):
        del self.segments[n]

    def lengthening_segment(self, n):
        seg = self.segments[n]
        seg.lengthen_segment()
        seg_next_1 = self.segments[n+1]
        seg_next_1.move_segment_lengthening(seg)
        #jeśli kolejny jest ostatnim
        if len(self.segments)-1 == n+1:
            # dodaje nowy który dotrze w jego miejsce
            self.add_segment(Segment(copy.deepcopy(seg_next_1.end_point), get_opposite_direction(seg.direction), copy.deepcopy(self.link.end_point), 1))

        else:
            #print(self.segments)
            seg_next_2 = self.segments[n+2]
            #jak trzeci ma ten sam kierunek
            if seg_next_2.direction == seg.direction:
                if seg_next_2.length > 1:
                    #skracanie
                    seg_next_2.shorten_segment_back()
                elif seg_next_2 == self.segments[-1]:
                    #usuwanie
                    self.segments.remove(seg_next_2)
                else:
                    #łaczenie

                    if self.segments[n+3].direction == seg_next_1.direction:
                        self.segments[n+3].start_point = copy.deepcopy(seg_next_1.start_point)
                        self.segments[n + 3].length += seg_next_1.length
                        self.segments.remove(seg_next_1)
                        self.segments.remove(seg_next_2)
                    else:
                        #odwrócenie zmian, jak idzie na nas
                        seg_next_1.move_segment_shortening(seg)
                        seg.shorten_segment()
            #trzeci ma inny kierunek

            else:
                #wydłuzyc
                seg_next_2.lengthen_segment_back()


    def shortening_segment(self, n):
        seg = self.segments[n]
        seg.shorten_segment()
        seg_next_1 = self.segments[n + 1]
        seg_next_1.move_segment_shortening(seg)

        # jesli kolejny jest ostatnim
        if len(self.segments)-1 == n+1:
            # dodaje nowy który dotrze w jego miejsce
            self.add_segment(Segment(copy.deepcopy(seg_next_1.end_point), seg.direction, copy.deepcopy(self.link.end_point), 1))
        else:
            seg_next_2 = self.segments[n+2]
            # trzeci w innym kierunku
            if seg_next_2.direction != seg.direction:
                if seg_next_2.length > 1:
                    #skracanie
                    seg_next_2.shorten_segment_back()
                elif seg_next_2 == self.segments[-1]:
                    #usuwanie
                    self.segments.remove(seg_next_2)
                else:
                    #laczenie
                    if self.segments[n + 3].direction == seg_next_1.direction:
                        self.segments[n + 3].start_point = copy.deepcopy(seg_next_1.start_point)
                        self.segments[n + 3].length += seg_next_1.length
                        self.segments.remove(seg_next_1)
                        self.segments.remove(seg_next_2)
                    else:
                        #odwrócenie zmian, jak idzie na nas
                        seg_next_1.move_segment_lengthening(seg)
                        seg.lengthen_segment()
            # trzeci w tym samym kierunku
            else:
                seg_next_2.lengthen_segment_back()

    def __repr__(self):
        return_string = "LINK: " + str(self.link) + "\n"
        for seg in self.segments:
            return_string += "SEGMENT: " + str(seg) + "\n"
        return return_string
