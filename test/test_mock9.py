from unittest import TestCase, expectedFailure
from unittest.mock import Mock, patch
from test.worker.collector import from_args


class TestMock9(TestCase):

	def test_patch_method(self):
		with patch('test.worker.collector.from_args') as mock_from_args:
			mock_from_args.return_value = 20

			print(str(from_args()))
