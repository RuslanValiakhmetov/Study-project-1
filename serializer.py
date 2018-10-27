import pickle
from figure import Triangle, Square


class Serializer:
    def __init__(self, side_length):
        self._figures_list = [Triangle(side_length), Square(side_length)]
        self._sum_areas = 0

    @property
    def figures_list(self):
        return self._figures_list

    @property
    def sum_areas(self):
        return self._sum_areas

    @sum_areas.setter
    def sum_areas(self, sum_areas):
        self._sum_areas = sum_areas

    @staticmethod
    def deserialize(data):
        return pickle.loads(data)

    def serialize(self):
        return pickle.dumps(self)

    def print_objects(self):
        for figure in self._figures_list:
            print(figure)
        print("Areas sum: {}".format(self._sum_areas))

    def update_figures(self, side_length):
        for figure in self._figures_list:
            figure.side_length = side_length
