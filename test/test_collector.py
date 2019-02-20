import unittest


def add(x, y):
	return x + y


class TestCollector(unittest.TestCase):
	a = 15
	b = 25

	def setUp(self):
		# Tests can be numerous, and their set-up can be repetitive. 
		# Luckily, we can factor out set-up code by implementing a method called setUp(), 
		# which the testing framework will automatically call for every single test we run:
		name = self.shortDescription()
		if name == 'add':
			self.a = 10
			self.b = 20
			print(name, self.a, self.b)
		elif name == 'sub':
			self.a = 50
			self.b = 60
			print(name, self.a, self.b)

	@classmethod
	def setUpClass(cls):
		print('Called once before any tests in class')

	def test_upper(self):
		self.skipTest("another method for skipping")
		self.assertEqual('foo'.upper(), 'FOO')

	@unittest.skip("demonstrating skipping")
	def test_is_upper(self):
		self.assertTrue('FOO'.isupper())
		self.assertTrue('Foo'.isupper())

	def test_add(self):
		"""add"""
		result = self.a +self.b
		self.assertEqual(result, 30)

	@unittest.skipIf(a > b, "Skip over this routine")
	def test_sub(self):
		"""sub"""
		result = self.a-self.b
		self.assertTrue(result == -10)

	@classmethod
	def tearDownClass(cls):
		print('Called once after all tests in class')

	def tearDown(self):
		# we can provide a tearDown() method that tidies up after every test method has been run:
		print('end of the test: ', self.shortDescription())
		

def arithmetic_test_suite():
	suite = unittest.TestSuite()
	suite.addTest(TestCollector('test_add'))
	suite.addTest(TestCollector('test_sub'))
	return suite

def get_test_suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(TestCollector))
	return suite

# if __name__ == '__main__':
# 	unittest.main()

# suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
# unittest.TextTestRunner(verbosity=2).run(suite)


# To run the Test Suite
suite = get_test_suite()
runner = unittest.TextTestRunner()
test_result = runner.run(suite)

print('No. of tests run', test_result.testsRun)