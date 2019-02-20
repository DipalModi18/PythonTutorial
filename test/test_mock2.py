from unittest import TestCase
from unittest.mock import patch, Mock
import myFolder


class TestBlog(TestCase):
	@patch('myFolder.Blog')
	def test_blog_posts(self, MockBlog):
		"""When a function is decorated using @patch,
			a mock of the class, method or function passed as the target to @patch is returned and
			passed as an argument to the decorated function."""
		# Instead of specifying patch before method definition and passed as an argument,
		# It can also be specified in the function body as
		#  with mock.patch('myFolder.Blog') as MockBlog:
		# 		xxx
		# 		Note: 'as' in the context manager is optional. Eg. with mock.patch('myFolder.Blog', return_value='testing'):
		blog = MockBlog()

		blog.posts.return_value = [{
			'userId': 1,
			'id': 1,
			'title': 'Test Title',
			'body': 'Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy\
			lies a small unregarded yellow sun.'
		}]

		response = blog.posts()
		print('blog posts response')
		print(response)
		self.assertIsNotNone(response)
		self.assertIsInstance(response[0], dict)

		# MagicMock, a subclass of Mock that implements default magic or dunder methods.
		# This makes MagicMock ideal to mock class behaviour, which is why it’s the default class when patching.
		print('MockBlog type: ', type(MockBlog))

		# Additional assertions
		assert MockBlog is myFolder.Blog  # The mock is equivalent to the original

		assert MockBlog.called  # The mock wasP called

		print('blog.post called with: ' + str(blog.posts.assert_called_with()))
		# We called the posts method with no arguments

		print('blog.posts.assert_called_once_with(): ' + str(blog.posts.assert_called_once_with()))
		# We called the posts method once with no arguments

		# blog.posts.assert_called_with(1, 2, 3) -
		# This assertion is False and will fail since we called blog.posts with no arguments

		blog.reset_mock()  # Reset the mock object

		blog.posts.assert_not_called()  # After resetting, posts has not been called.
