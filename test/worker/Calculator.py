# This class is used in test_mock2
import time


class Calculator:
	def sum(self, a, b):
		time.sleep(20)
		return a + b
