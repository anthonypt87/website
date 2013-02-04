import models
from django.test import TestCase


class BlogModelTest(TestCase):

	def setUp(self):
		self.created_category = models.Category(
			title='category_title',
			slug='category_slug'
		)
		self.created_category.save()
		self.created_blog = models.Blog(
			title='Title',
			slug='Slug',
			body='Body',
			category=self.created_category
		)
		self.created_blog.save()

	def tearDown(self):
		self.created_blog.delete()

	def test_model_works(self):
		loaded_blog = models.Blog.objects.get(id=self.created_blog.id)
		self.assertEqual(
			loaded_blog,
			self.created_blog
		)

