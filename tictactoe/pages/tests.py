from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client

# Create your tests here.

class ProjectTest(TestCase):

	def test_homepage(self):
		c = Client()
		response = c.get(reverse('home'))
		self.assertEqual(response.status_code, 200)