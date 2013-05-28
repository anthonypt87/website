from blog import models
from django.test import TestCase


class EntryModelTest(TestCase):

	def setUp(self):
		self.created_category = models.Category(
			title='category_title',
			slug='category_slug'
		)
		self.created_category.save()
		self.created_entry = models.Entry(
			title='Title',
			slug='Slug',
			body='Body',
			category=self.created_category
		)
		self.created_entry.save()

	def tearDown(self):
		self.created_entry.delete()

	def test_model_works(self):
		loaded_entry = models.Entry.objects.get(id=self.created_entry.id)
		self.assertEqual(
			loaded_entry,
			self.created_entry
		)

