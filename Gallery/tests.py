from django.test import TestCase
from .models import PostFeed
from django_webtest import WebTest
# Create your tests here.
class PostFeedTestCase(TestCase):

		def test_str_repr(self):
				postfeed = PostFeed(newsfeed="this is a test title")
				self.assertEqual(str(postfeed), postfeed.newsfeed)

class HomeListViewTest(WebTest):

		def test_one_post(self):
				PostFeed.objects.create(newsfeed="title")
				response = self.client.get('/')
				self.assertContains(response, "title")

		def test_two_post(self):
				PostFeed.objects.create(newsfeed="title is new")
				PostFeed.objects.create(newsfeed="title is newer")
				response = self.client.get('/')
				self.assertContains(response, "title is new")
				self.assertContains(response, "title is newer")

		def test_no_post(self):
				response = self.client.get('/')
				self.assertContains(response, "We are sorry but we have no newsfeed to display right now!")