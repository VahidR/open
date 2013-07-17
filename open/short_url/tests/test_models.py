from django.test import TestCase

from short_url.models import Link


class TestLink(TestCase):
	'''
	This is a class for testin ``Link`` Model.
	'''

	def setUp(self):
		self.Link1 = Link.objects.create(url = "www.google.com")

	def tearDown(self):
		Link.objects.all().delete()

	def test_link_model_is_unicode(self):
		self.assertEquals(unicode(self.Link1), "www.google.com")
	
	def test_link_model_produces_hash(self):
		self.assertTrue(self.Link1.hash_code)
