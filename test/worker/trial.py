import random


class Trial:
	a = None

	def __init__(self):
		self.a = 5

	def first_method(self):
		print('In first method')

	def second_method(self, no):
		print('In second_method')
		if no >= 5:
			self.first_method()

	def third_method(self):
		random_num = random.randrange(0, 10)
		print('random_num: ', random_num)
		self.second_method(random_num)
		return 8

	def get_exception(self):
		raise Exception('Returning the exception')

	def return_something(self):
		return None

	def call_return_something(self):
		return self.return_something()


class Trial2:
	@classmethod
	def return_something_class_method(self):
		return None

	@classmethod
	def call_return_something_class_method(cls):
		return cls.return_something_class_method()


class Temp:
	def temp_method(self):
		trial = Trial()
		print('Created trial obj')
		return trial.third_method()
