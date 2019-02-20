from unittest import TestCase
from unittest.mock import patch
import test.worker


def mock_sum(a, b):
	# mock sum function without the long running time.sleep as in myFolder.Calculator
	return a + b


class TestCalculator3(TestCase):

	@patch('test.worker.Calculator.sum', side_effect=mock_sum)
	def test_sum(self, MockSum):
		self.assertEqual(MockSum(2, 3), 5)
		self.assertEqual(MockSum(4, 5), 9)
