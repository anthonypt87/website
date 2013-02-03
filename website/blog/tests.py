import models
from django.test import TestCase


class BlogModelTest(TestCase):

	def setUp(self):
		self.created_category = models.Category(
			title='category_title',
			slug='category_slug'
		)
		self.created_blog = models.Blog(
			title='Title',
			slug='Slug',
			body='Body',
			category=self.created_category.id
		)

	def tearDown(self):
		self.created_blog.delete()

	def test_model_works(self):
		loaded_blog = self.created_blog.get(id=self.created_blog.id)
		self.assertEqual(
			loaded_blog,
			self.created_blog
		)

