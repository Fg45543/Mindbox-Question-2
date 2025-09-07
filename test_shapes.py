import unittest
import math
from shapes import Circle, Triangle, calculate_area


class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)

    def test_circle_invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)

    def test_right_angled_triangle(self):
        self.assertTrue(Triangle(3, 4, 5).is_right_angled())
        self.assertFalse(Triangle(3, 4, 6).is_right_angled())

    def test_calculate_area_polymorphism(self):
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = [calculate_area(s) for s in shapes]
        self.assertAlmostEqual(areas[0], math.pi * 4)
        self.assertAlmostEqual(areas[1], 6.0)


if __name__ == '__main__':
    unittest.main()