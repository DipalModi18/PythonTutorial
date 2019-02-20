from unittest import TestCase, mock, expectedFailure
import unittest
from test.worker.Calculator import Calculator
from test.worker.trial import Trial, Trial2, Temp


class TestMock7(TestCase):
	def test_mocking_class(self):
		print('name: ', __name__)
		mock_calc = mock.MagicMock(spec=Calculator)
		mock_calc.sum(3, 4)

	@mock.patch('test.worker.trial.Trial.first_method')
	def test_assert_if_method_called(self, mock_first_method):
		"""Check if first_method has been called from inside of the second_method"""
		trial = Trial()
		trial.second_method(7)
		self.assertTrue(mock_first_method.called)

	@mock.patch('test.worker.trial.Trial.first_method')
	def test_assert_if_method_not_called(self, mock_first_method):
		"""Check if first_method has been called from inside of the second_method"""
		trial = Trial()
		trial.second_method(3)
		self.assertFalse(mock_first_method.called)

	def test_assert_raises_success(self):
		self.assertRaises(ZeroDivisionError, lambda: 5/0)
		# syntax: self.assertRaises(expected_exception, expression_which_will_throw_the_expected_exception)
		# Expected ZeroDivisionError and expression raised the ZeroDivisionError. So this test will not fail

	def test_assert_raises_success2(self):
		trial = Trial()
		self.assertRaises(Exception, lambda: trial.get_exception())
		# Even for the function, lambda will be required to wrap the function call

	def test_assert_raises_success3(self):
		trial = Trial()
		with self.assertRaises(Exception):
			trial.get_exception()
		# Instead of using lambda to wrap the expression, this can be used as a better solution

	@expectedFailure
	def test_assert_raises_failure(self):
		self.assertRaises(ZeroDivisionError, 5/0)
		# This case same as above without lambda
		# Used lambda to have a wrapper around the the expression,
		# otherwise assertRaises throws error which will consequence in failure of the test case

	@expectedFailure
	def test_assert_raises_failure2(self):
		self.assertRaises(ValueError, lambda: 5/0)
		# Expected ValueError and expr raise ZeroDivisionError.
		# If a different type of exception is raised, it will not be caught, and the test case will be deemed to have
		# suffered an error, exactly as for an unexpected exception.

	@expectedFailure
	def test_assert_raises3(self):
		self.assertRaises(ZeroDivisionError, lambda: 5/1)
		# Expected ZeroDivisionError and expr raised no exception at all

	def test_can_assign_value(self):
		value = 'modi'
		trial = Trial()
		trial.name = value
		print(trial.name)

	def test_if_none(self):
		temp = None
		if not temp:
			print('temp not none')
		else:
			print('temp is none')

	@mock.patch('test.worker.trial.Trial.return_something')
	def test_change_return_value(self, mock_return_something_call):
		mock_return_something_call.return_value = 1
		trial = Trial()
		response = trial.call_return_something()
		print('Response: ' + str(response) + ' type: ' + str(type(response)))

	@mock.patch('test.worker.trial.Trial2.return_something_class_method')  # Same as earlier
	def test_change_return_value_of_class_method(self, mock_return_something_call):
		mock_return_something_call.return_value = 1
		# trial = Trial2()
		# response = trial.call_return_something_class_method()
		response = Trial2.call_return_something_class_method()
		print('Response: ' + str(response) + ' type: ' + str(type(response)))

	@mock.patch('test.worker.trial.Trial.third_method')
	def test_change_return_value(self, mock_third_method_call):
		mock_third_method_call.return_value = 15
		temp = Temp()
		print('temp_method returns: ' + str(temp.temp_method()))


if __name__ == '__main__':
	unittest.main()
