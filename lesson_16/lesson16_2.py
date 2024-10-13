from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area_figure(self):
        pass

    @abstractmethod
    def perimetr_figure(self):
        pass


class Square(Figure):
    def __init__(self, side_a):
        self.__side_a = side_a

    def area_figure(self):
        return self.__side_a ** 2

    def perimetr_figure(self):
        return 4 * self.__side_a


class Rhombus(Figure):
    def __init__(self, side_a, high):
        self.__side_a = side_a
        self.__high = high

    def area_figure(self):
        return self.__side_a * self.__high

    def perimetr_figure(self):
        return 4 * self.__side_a


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def area_figure(self):
        return self.__side_a * self.__side_b

    def perimetr_figure(self):
        return 2 * (self.__side_a + self.__side_b)


figures = [Square(10), Rhombus(10, 2), Rectangle(10, 2)]

for fig in figures:
    print(f"Figure: {fig.__class__.__name__}")
    print(f"Area: {fig.area_figure()}")
    print(f"Perimetr: {fig.perimetr_figure()}\n")
