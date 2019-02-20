import unittest
from unittest import mock, TestCase
from test.worker.worker2 import work_on, size_of
from io import StringIO


class TestBuiltin(TestCase):

	# @mock.patch('os.getcwd', return_value='/home/')
	# @mock.patch('worker.print')
	# @mock.patch.dict('os.environ', {'MY_VAR': 'testing'})
	def test_patch_dict(self):
		with mock.patch('test.worker.worker2.print') as mock_print:
			with mock.patch('os.getcwd', return_value='/home/'):

				# we are using patch.dict to inject a temporary environment variable in os.environ, this is extensible to any other
				# dictionary we would like to mock.
				with mock.patch.dict('os.environ', {'MY_VAR': 'testing'}):
					self.assertEqual(work_on(), '/home/testing')
					mock_print.assert_called_once_with('Working on /home/testing')

	def test_context_manager(self):
		with mock.patch('test.worker.worker2.open') as mock_open:

			# https://docs.python.org/3/reference/datamodel.html#object.__enter__
			mock_open.return_value.__enter__.return_value = StringIO('testing')
			self.assertEqual(size_of(), 7)


if __name__ == '__main__':
	unittest.main()
