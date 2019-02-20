import unittest
from unittest import mock, TestSuite, TextTestRunner
from unittest import TestCase


class TestMock4(TestCase):

	def test_mock(self):
		m = mock.Mock()
		assert isinstance(m.foo, mock.Mock)
		assert isinstance(m.bar, mock.Mock)
		assert isinstance(m(), mock.Mock)
		m.foo = 'bar'
		assert m.foo == 'bar'

		# Set attributes on the mock through keyword arguments.
		m.configure_mock(name='dipal')
		# configure_mock() exists to make it easier to do configuration after the mock has been created.
		assert m.name == 'dipal'

	def test_mock2(self):
		m = mock.Mock()
		m.return_value = 42
		assert m() == 42

		# if you’d like to return different values on each call you can assign an iterable to side_effect.
		m.side_effect = ['foo', 'bar', 'baz']
		assert m() == 'foo'
		assert m() == 'bar'
		assert m() == 'baz'
		try:
			m()
		except StopIteration:
			assert True
		else:
			assert False

		print('mock called for ', m.call_count, ' times')

		# If you’d like to raise an exception when calling the Mock you can simply assign the exception object to side_effect.
		m.side_effect = RuntimeError('Boom')
		try:
			m()
		except RuntimeError:
			assert True
		else:
			assert False


# suite = TestSuite()
# suite.addTest(unittest.makeSuite(TestMock4))
# runner = TextTestRunner()
# result = runner.run(suite)
