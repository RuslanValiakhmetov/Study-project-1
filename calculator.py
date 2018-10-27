from math import pow
from serializer import Serializer


class Calculator:
    def __init__(self, side_length):
        self._serializer = Serializer(side_length)
        self._file_name = "serializer.bin"

    @property
    def serializer(self):
        return self._serializer

    def calculate_sum_area(self):
        sum_areas = 0
        # пример полиморфизма
        for figure in self._serializer.figures_list:
            figure.calc_area()
            sum_areas += figure.area
        self._serializer.sum_areas = round(sum_areas)

    def save(self):
        with open(self._file_name, "wb") as file:
            file.write(self._serializer.serialize())
            file.flush()
            file.close()

    def restore(self):
        with open(self._file_name, "rb") as file:
            self._serializer = Serializer.deserialize(file.read())
            file.close()

    def show(self):
        self._serializer.print_objects()

    def update_figures(self, side_length):
        self._serializer.update_figures(side_length)
        if self._serializer.sum_areas != 0:
            self.calculate_sum_area()

    @staticmethod
    # Метод перевода числа из двоичного в десятичное представление
    def binary_to_integer(binary_value):
        """
        This function converts binary value as a string to decimal integer value
        :param binary_value: string binary value
        :return: decimal integer value
        """
        integer_value = 0
        binary_index = 0
        # Реверсивный обход строки
        for char in binary_value[::-1]:
            if char == '1':
                integer_value += pow(2, binary_index)
            binary_index += 1

        return int(integer_value)
