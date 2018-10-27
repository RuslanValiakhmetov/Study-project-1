from math import pow


class Figure:
    def __init__(self, side_length):
        self._side_length = side_length
        self._area = 0

    def __str__(self):
        """
        Abstract method - must be implemented by subclasses
        :return: Noting
        """
        raise NotImplementedError

    def calc_area(self):
        """
        Abstract method - must be implemented by subclasses
        :return: Noting
        """
        raise NotImplementedError()

    @property
    def side_length(self):
        return self._side_length

    @side_length.setter
    def side_length(self, side_length):
        self._side_length = side_length

    @property
    def area(self):
        return self._area


class Triangle(Figure):
    def __str__(self):
        """
        returns object in string representation
        :return:
        """
        return "Figure: %s(side length = %d; area = %.2f)" % \
               (Triangle.__name__, self.side_length, self._area)

    def calc_area(self):
        self._area = round(pow(3, (1. / 3)) * pow(self._side_length, 2) / 4, 2)


class Square(Figure):
    def __str__(self):
        return "Figure: %s(side length = %d; area = %d)" % \
               (Square.__name__, self.side_length, self._area)

    def calc_area(self):
        self._area = int(pow(self._side_length, 2))
