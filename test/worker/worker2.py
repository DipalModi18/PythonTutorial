"""Used in mocking_classes.py"""

import os


def work_on():
	path = os.path.join(os.getcwd(), os.environ['MY_VAR'])
	print('Working on ' + path)
	return path


def size_of():
	with open('worker.py') as file:
		contents = file.read()

	return len(contents)


class Pricer:
	DISCOUNT = 0.8

	def get_discounted_price(self, price):
		return price * self.DISCOUNT
