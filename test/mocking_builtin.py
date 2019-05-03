import unittest
from unittest import mock, TestCase
from worker.worker2 import work_on, size_of
from io import StringIO


class TestBuiltin(TestCase):

	# @mock.patch('os.getcwd', return_value='/home/')
	# @mock.patch('worker.print')
	# @mock.patch.dict('os.environ', {'MY_VAR': 'testing'})
	def test_patch_dict(self):
		with mock.patch('worker.worker2.print') as mock_print:  # Mocking default print function
			with mock.patch('os.getcwd', return_value='/home/'):  # Mocking the behavior of getcwd method of os package

				# we are using patch.dict to inject a temporary environment variable in os.environ, this is extensible to any other
				# dictionary we would like to mock.
				with mock.patch.dict('os.environ', {'MY_VAR': 'testing'}):
					self.assertEqual(work_on(), '/home/testing')
					mock_print.assert_called_once_with('Working on /home/testing')

	# A context manager is an object that defines the runtime context to be established when executing a with statement.
	# The context manager handles the entry into, and the exit from,
	#   the desired runtime context for the execution of the block of code.
	# Context managers are normally invoked using the with statement, but can also be used by
	#   directly invoking their methods.
	# Typical uses of context managers include saving and restoring various kinds of global state,
	#   locking and unlocking resources, closing opened files, etc.
	def test_context_manager(self):
		with mock.patch('worker.worker2.open') as mock_open:

			# https://docs.python.org/3/reference/datamodel.html#object.__enter__ :
			#   Enter the runtime context related to this object.
			mock_open.return_value.__enter__.return_value = StringIO('testing')  # To mock the open method using _enter_
			self.assertEqual(size_of(), 7)


if __name__ == '__main__':
	unittest.main()

# To run: python3 test/mocking_builtin.py
