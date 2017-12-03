#######################################################
# This is a programme to test the functionality of the 
# calculator.py programme to confirm results are as 
# expected.
#
# Scripted by Andrew Doran-Sherlock 10361540
# 05 October 2017
#######################################################


import unittest
from list_calculator import Calculator

# test the calculator functionality
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()


    # this tests the add functionality

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add([1,-2,3], [1,-2,3])
        self.assertEqual([2,-4,6], result)

		
	# this tests the subtract functionality

    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract([1,-2,3], [1,5,-9])
        self.assertEqual([0,-7,12], result)
        

# this test the multiply functionality

    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply([1,-2,-3], [0,-4,5])
        self.assertEqual([0,8,-15], result)

		
	# this tests the division functionality


    def test_calculator_divide_method_returns_correct_result(self):
        result = self.calc.divide([1,-2,6], [1,2,3])
        self.assertEqual([1,-1,2], result)

		
	# this tests the exponential functionality

    def test_calculator_exponential_method_returns_correct_result(self):
        result = self.calc.exponential([1,2,-3], [-10,3,2])
        self.assertEqual([1,8,9], result)

		
	# this tests the square root functionality

    def test_calculator_square_root_method_returns_correct_result(self):
        result = self.calc.square_root([1,4,9])
        self.assertEqual([1,2,3], result)

		
	# this tests the sine functionality

    def test_calculator_sine_method_returns_correct_result(self):
        result = self.calc.sine([0.0,0.5,1.0])
        self.assertEqual([0.0,0.47943,0.84147], result)

		
	# this tests the cosine functionality

    def test_calculator_cosine_method_returns_correct_result(self):
        result = self.calc.cosine([0.0,0.5,1.0])
        self.assertEqual([1.0,0.87758,0.5403], result)


	# this tests the squaring functionality

    def test_calculator_square_method_returns_correct_result(self):
        result = self.calc.square([0.5,-3,12])
        self.assertEqual([0.25,9,144], result)


	# this tests the cubing functionality

    def test_calculator_cube_method_returns_correct_result(self):
        result = self.calc.cube([0.5,3,-4])
        self.assertEqual([0.125,27,-64], result)
	


if __name__ == '__main__':
    unittest.main()
