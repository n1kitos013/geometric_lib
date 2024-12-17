import sys
import unittest

sys.path.append("/Users/User/geometric_lib")
import calculate


class TestSquareArea(unittest.TestCase):

    def test_first_area(self):
        fig = "square"
        func = "area"
        size = [10]
        result = calculate.calc(fig, func, size)
        expected_result = 100

        self.assertEqual(result, expected_result)

    def test_second_area(self):
        fig = "square"
        func = "area"
        size = [-10]
        result = calculate.calc(fig, func, size)
        expected_result = 404

        self.assertEqual(result, expected_result)

    def test_third_area(self):
        fig = "square"
        func = "area"
        size = [10**9]
        result = calculate.calc(fig, func, size)
        expected_result = 10**18

        self.assertEqual(result, expected_result)


class TestSquarePerimeter(unittest.TestCase):

    def test_first_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [10]
        result = calculate.calc(fig, func, size)
        expected_result = 40

        self.assertEqual(result, expected_result)

    def test_second_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [-10]
        result = calculate.calc(fig, func, size)
        expected_result = 404

        self.assertEqual(result, expected_result)

    def test_third_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [10**9]
        result = calculate.calc(fig, func, size)
        expected_result = 10**9 * 4

        self.assertEqual(result, expected_result)


class TestTriangleArea(unittest.TestCase):

    def test_first_area(self):
        fig = "triangle"
        func = "area"
        size = [10, 10, 10]
        result = calculate.calc(fig, func, size)
        expected_result = 43.30127018922193

        self.assertEqual(result, expected_result)

    def test_second_area(self):
        fig = "triangle"
        func = "area"
        size = [-10, 10, 10]
        result = calculate.calc(fig, func, size)
        expected_result = 404

        self.assertEqual(result, expected_result)

    def test_third_area(self):
        fig = "triangle"
        func = "area"
        size = [10, 20, 30]
        result = calculate.calc(fig, func, size)
        expected_result = 404

        self.assertEqual(result, expected_result)


class TestTrianglePerimeter(unittest.TestCase):

    def test_first_perimeter(self):
        fig = "triangle"
        func = "perimeter"
        size = [10, 10, 10]
        result = calculate.calc(fig, func, size)
        expected_result = 30

        self.assertEqual(result, expected_result)

    def test_second_perimeter(self):
        fig = "triangle"
        func = "perimeter"
        size = [-10, 10, 10]
        result = calculate.calc(fig, func, size)
        expected_result = 404

        self.assertEqual(result, expected_result)

    def test_third_perimeter(self):
        fig = "triangle"
        func = "perimeter"
        size = [10, 20, 30]
        result = calculate.calc(fig, func, size)
        expected_result = 404

        self.assertEqual(result, expected_result)


class TestCircleArea(unittest.TestCase):

    def test_first_area(self):
        fig = "circle"
        func = "area"
        size = [10]
        result = calculate.calc(fig, func, size)
        expected_result = 314.1592653589793

        self.assertEqual(result, expected_result)

    def test_second_area(self):
        fig = "circle"
        func = "area"
        size = [-10]
        result = calculate.calc(fig, func, size)
        expected_result = 404

        self.assertEqual(result, expected_result)

    def test_third_area(self):
        fig = "circle"
        func = "area"
        size = [10**9]
        result = calculate.calc(fig, func, size)
        expected_result = 3.1415926535897933e18

        self.assertEqual(result, expected_result)


class TestCirclePerimeter(unittest.TestCase):

    def test_first_perimeter(self):
        fig = "circle"
        func = "perimeter"
        size = [10]
        result = calculate.calc(fig, func, size)
        expected_result = 62.83185307179586

        self.assertEqual(result, expected_result)

    def test_second_perimeter(self):
        fig = "circle"
        func = "perimeter"
        size = [-10]
        result = calculate.calc(fig, func, size)
        expected_result = 404

        self.assertEqual(result, expected_result)

    def test_third_perimeter(self):
        fig = "circle"
        func = "perimeter"
        size = [10**9]
        result = calculate.calc(fig, func, size)
        expected_result = 6283185307.179586

        self.assertEqual(result, expected_result)
