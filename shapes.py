import math
from abc import ABC, abstractmethod
from typing import Union


class Shape(ABC):
    #Абстрактный базовый класс для геометрических фигур."""

    @abstractmethod
    def area(self) -> float:
        #Вычисляет площадь фигуры
        pass

    @abstractmethod
    def is_right_angled(self) -> bool:
        #Проверяет, является ли фигура прямоугольной (если применимо)
        pass


class Circle(Shape):
    #Класс для представления круга

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def is_right_angled(self) -> bool:
        #Круг не может быть прямоугольным, всегда возвращает False
        return False


class Triangle(Shape):
    #Класс для представления треугольника

    def __init__(self, a: float, b: float, c: float):
        # Проверка валидности сторон
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("Все стороны должны быть положительными числами")
        if not self._is_valid_triangle(a, b, c):
            raise ValueError("Треугольник с такими сторонами не существует")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        # Формула Герона
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self, tolerance: float = 1e-6) -> bool:
        #Проверяет, является ли треугольник прямоугольным с заданной точностью
        sides = sorted([self.a, self.b, self.c])
        # Проверка теоремы Пифагора
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < tolerance

    def _is_valid_triangle(self, a: float, b: float, c: float) -> bool:
        #Проверяет, может ли треугольник существовать.
        return (a + b > c) and (a + c > b) and (b + c > a)


def calculate_area(shape: Shape) -> float:
    #Вычисляет площадь любой фигуры без знания её типа в compile-time
    return shape.area()
