# Now there is two things we need to test:

# Worker calls Helper with "db"
# Worker returns the expected path supplied by Helper
from unittest import mock, TestCase, expectedFailure
from test.worker.worker import Helper, Worker
from test.worker.worker2 import Pricer


class TestWorkerClass(TestCase):

	def test_patching_class(self):
		# simply pass autospec = True to the patch call, which will configure the Mock to behave as the object being mocked,
		# raising exceptions for missing attributes and incorrect signatures as required.
		with mock.patch('test.worker.worker.Helper', autospec=True) as MockHelper:

			# simply using MockHelper.get_path.return_value would not work since in the code we call get_path on an instance,
			# not the class itself.
			MockHelper.return_value.get_path.return_value = 'testing'

			worker = Worker()
			MockHelper.assert_called_once_with('db')
			self.assertEqual(worker.work(), 'testing')

	# If you are less inclined to testing in complete isolation you can also partially patch a class using patch.object
	def test_partial_patching(self):
		with mock.patch.object(Helper, 'get_path', return_value='testing'):
			# patch.object is allowing us to configure a mocked version of get_path only,
			# leaving the rest of the behaviour untouched
			worker = Worker()
			self.assertEqual(worker.helper.path, 'db')
			self.assertEqual(worker.work(), 'testing')

	def test_patch_class_attribute(self):
		with mock.patch.object(Pricer, 'DISCOUNT', 1):
			# Inside this clause, DISCOUNT will have value 1
			pricer = Pricer()
			print('DISCOUNT: ', pricer.DISCOUNT)
			self.assertAlmostEqual(pricer.get_discounted_price(100), 100)

		# Outside with, it will not follow the patched value for DISCOUNT
		self.assertAlmostEqual(pricer.get_discounted_price(100), 80)

	@expectedFailure
	def test_patch_incorrect_class_attribute(self):
		with mock.patch.object(Pricer, 'Percentage', 1):
			pricer = Pricer()
			self.assertEqual(pricer.get_discounted_price(100), 100)

	@mock.patch.object(Helper, 'get_a', return_value='aa')
	@mock.patch.object(Helper, 'get_b', return_value='bb')
	def test_multiple_patches(self, MockGetB, MockGetA):  # Order is reverse to get the mock for methods
		print('Get a: ', MockGetA())
		print('Get b: ', MockGetB())


