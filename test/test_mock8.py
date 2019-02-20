from unittest import TestCase, expectedFailure
from unittest.mock import Mock, patch
from test.worker.trial import Temp, Trial


@patch('test.worker.trial.Temp.temp_method')  # To patch in all test cases
class TestMock8(TestCase):

	def setUp(self):
		mock_sum = Mock()

	@patch('test.worker.trial.Temp')
	def test_all_method(self, mock_temp, mock_temp_method):
		mock_temp_obj = Mock()
		mock_temp.return_value = mock_temp_obj
		mock_temp.return_value.third_method.return_value = 5
		print('Before temp called')
		mock_temp_obj.temp_method()

	# @patch('test.worker.trial.Temp.temp_method')
	@patch('test.worker.trial.Trial')
	def test_common_patch1(self, mock_trial, mock_temp_method):
		temp = Temp()
		temp.temp_method()
		self.assertTrue(mock_temp_method.called)

		mock_trial.return_value = Mock()
		mock_trial.return_value.first_method.return_value = 2
		trial = Trial()

	# @patch('test.worker.trial.Temp.temp_method')
	def test_common_patch2(self, mock_temp_method):
		temp = Temp()
		self.assertFalse(mock_temp_method.called)
