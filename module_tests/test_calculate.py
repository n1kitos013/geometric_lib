import unittest
import sys
sys.path.append("/Users/User/geometric_lib")
import calculate

class TestCalculate(unittest.TestCase):

    def test_circle_perimeter(self):
        result = calculate.calc('circle', 'perimeter', [5])
        self.assertEqual(result, 31.41592653589793)  
    
    def test_circle_area(self):
        result = calculate.calc('circle', 'area', [5])
        self.assertAlmostEqual(result, 78.53981633974483) 

    def test_square_perimeter(self):
        result = calculate.calc('square', 'perimeter', [5])
        self.assertEqual(result, 20)

    def test_square_area(self):
        result = calculate.calc('square', 'area', [5])
        self.assertEqual(result, 25)

    def test_triangle_perimeter(self):
        result = calculate.calc('triangle', 'perimeter', [3, 4, 5])
        self.assertEqual(result, 12)

    def test_triangle_area(self):
        result = calculate.calc('triangle', 'area', [3, 4, 5])
        self.assertAlmostEqual(result, 6.0)  

    def test_triangle_invalid_sides(self):
        result = calculate.calc('triangle', 'perimeter', [1, 2, 5])
        self.assertEqual(result, "Can not make a triangle out of these elements")

    def test_invalid_input_positive(self):
        result = calculate.calc('circle', 'perimeter', [-5])
        self.assertEqual(result, "All elements must be positive!")
   
    def test_circle_perimeter_zero(self):
        result = calculate.calc('circle', 'perimeter', [0])
        self.assertEqual(result, "All elements must be positive!")

    def test_square_area_zero(self):
        result = calculate.calc('square', 'area', [0])
        self.assertEqual(result, "All elements must be positive!")

    def test_triangle_perimeter_zero(self):
        result = calculate.calc('triangle', 'perimeter', [0, 0, 0])
        self.assertEqual(result, "All elements must be positive!")

    def test_triangle_area_zero(self):
        result = calculate.calc('triangle', 'area', [3, 4, 5])
        self.assertAlmostEqual(result, 6.0)

    def test_triangle_area_zero_sides(self):
        result = calculate.calc('triangle', 'area', [0, 0, 0])
        self.assertEqual(result, "All elements must be positive!")

    def test_triangle_perimeter_large_sides(self):
        result = calculate.calc('triangle', 'perimeter', [100, 200, 300])
        self.assertEqual(result,"Can not make a triangle out of these elements")

    def test_triangle_area_large_sides(self):
        result = calculate.calc('triangle', 'area', [10, 10, 10])
        self.assertAlmostEqual(result, 43.30127018922193)  