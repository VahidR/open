from django.db import models
from django.conf import settings

import hashlib


class Link(models.Model):
	url = models.URLField()
	hash_code = models.CharField(max_length = 6, blank = True, db_index=True)

	def save(self, *args, **kwargs):
		self.hash_code = hashlib.md5(self.url).hexdigest()[:6]
		super(Link, self).save(*args, **kwargs)

	
	def shorten(self):
		return settings.SITE_BASE_URL + self.hash_code
	
	def __unicode__(self):
		return self.url

	def get_absolute_url(self):
		return settings.SITE_BASE_URL + self.hash_code
