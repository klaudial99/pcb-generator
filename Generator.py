from Point import Point
from Segment import Segment
import random
import AlgorithmParameters as ap

directions = {"NONE": 0,
              "UP": 1,
              "RIGHT": 2,
              "DOWN": 3,
              "LEFT": 4}


def valid_direction(direction, prev_direction): #dont go back

    if direction != 0:
        if prev_direction == 1 and direction != 3:
            return True
        elif prev_direction == 2 and direction != 4:
            return True
        elif prev_direction == 3 and direction != 1:
            return True
        elif prev_direction == 4 and direction != 2:
            return True
        elif prev_direction == 0 and direction != 0:
            return True
        else:
            return False
    else:
        return False


def random_direction():
    return random.randint(1, 4)


def move(start_point, direction):
    if direction == 1:
        return Point(start_point.x, start_point.y + 1)
    elif direction == 2:
        return Point(start_point.x + 1, start_point.y)
    elif direction == 3:
        return Point(start_point.x, start_point.y - 1)
    elif direction == 4:
        return Point(start_point.x - 1, start_point.y)


def proper_direction(path, actual_point, prev_direction):
    if prev_direction == 1 or prev_direction == 3:
        if path.link.end_point.x > actual_point.x:
            return 2
        else:
            return 4
    else:
        if path.link.end_point.y > actual_point.y:
            return 1
        else:
            return 3


class Generator:

    def __init__(self, individual):
        self.__individual = individual

    @property
    def individual(self):
        return self.__individual

    @individual.setter
    def individual(self, individual):
        self.__individual = individual

    def generate_random_paths(self):
        for single_path in self.individual.paths:
            actual_point = single_path.link.start_point
            end_point = single_path.link.end_point

            last_direction = 0
            last_point = actual_point
            i = 0
            while actual_point != end_point:  # until reach end point
                i += 1
                direction = 0

                random_number = random.randint(0, 100)
                if random_number < ap.PROPER_DIRECTION_PROBABILITY:
                    direction = proper_direction(single_path, last_point, last_direction)
                    actual_point = move(last_point, direction)

                else:
                    while not (valid_direction(direction, last_direction) and self.individual.pcb.check_point_on_board(actual_point)): #NAND
                        # until direction is valid (dont go back) and point is on a board
                        direction = random_direction()
                        actual_point = move(last_point, direction)  # nearby point

                if direction != last_direction and last_direction != 0:  # if direction changes
                    single_path.add_segment(Segment(last_point, direction, actual_point, 1))  # add new segment
                else:  # update current segment
                    edit_segment = single_path.segments[-1]
                    edit_segment.set_end_point(actual_point)
                    edit_segment.length += 1

                    if last_direction == 0: # first move
                        edit_segment.direction = direction
                    single_path.set_last_segment(edit_segment)

                last_direction = direction
                last_point = actual_point
            #print("ALL: " + str(i))
