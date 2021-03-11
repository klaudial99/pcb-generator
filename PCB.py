from Point import Point
from Link import Link


class PCB:

    def __init__(self, width=0, height=0, links_objects_list=None):
        if links_objects_list is None:
            links_objects_list = []

        self.__width = width
        self.__height = height

        self.__board_links = links_objects_list

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def board_links(self):
        return self.__board_links

    @board_links.setter
    def board_links(self, links_objects_list):
        self.__board_links = links_objects_list

    def check_point_on_board(self, point):
        if isinstance(point, Point):

            return 0 <= point.x < self.width and 0 <= point.y < self.height

    def read_from_file(self, path):
        try:
            with open(path, "r") as file:
                #SIZE
                size = file.readline().split(";")
                self.width = int(size[0])
                self.height = int(size[1])

                #LINKS
                for line in file.readlines():
                    points = line.split(";")
                    start_point = Point(int(points[0]), int(points[1]))
                    end_point = Point(int(points[2]), int(points[3]))

                    # creates link only if points are on the board
                    if self.check_point_on_board(start_point) and self.check_point_on_board(end_point):
                        link = Link(start_point, end_point)
                        self.board_links.append(link)
        except IOError:
            print("File not accesible")

    def __str__(self):
        return "WIDTH: " + str(self.width) + "\nHEIGHT: " + str(self.height) + "\nLINKS: " + str(self.board_links)


if __name__ == '__main__':
    pcb = PCB()
    pcb.read_from_file("D:/studia/6. sem/Sztuczna inteligencja i inżynieria wiedzy/Laborki/lista1/zad0.txt")
    print(pcb)


