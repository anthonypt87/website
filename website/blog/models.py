import datetime

from django.db import models
from django.utils import timezone

class Entry(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	time_posted = models.DateTimeField(db_index=True, auto_now_add=True)
	category = models.ForeignKey('blog.Category')

	def __unicode__(self):
		return self.title

	def was_published_recently(self):
		return self.time_posted >= timezone.now() - datetime.timedelta(days=1)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

	def __unicode__(self):
		return self.title
