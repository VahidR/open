from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class LinkIntegrationTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_user_can_shorten_a_link(self):
		self.browser.get(self.live_server_url)
		
		
		
		
		# OBS. This is intended to fail the test to remember of passing this functionality
		self.fail("TODO: navigate through the site and add a URL..")

