import unittest
from unittest import expectedFailure
from unittest.mock import patch
# mocking allows you to provide a so-called fake implementation of the part of your system you are testing.
from test.worker.Calculator import Calculator


class TestCalculator(unittest.TestCase):
	def setUp(self):
		self.calc = Calculator()

	# def test_sum(self):  # Without mocking => This Test case will take much longer time
	# 	answer = self.calc.sum(2, 4)
	# 	self.assertEqual(answer, 6)

	# We are importing the patch decorator from unittest.mock. 
	# It replaces the actual sum function with a mock function that behaves exactly how we want.
	@patch('test.worker.Calculator.sum', return_value=9)
	def test_sum(self, sum):
		self.assertEqual(sum(2, 3), 9)


# if __name__ == '__main__':
# 	unittest.main()
