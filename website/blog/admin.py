from django.contrib import admin
from blog import models

class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'posted')

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Category, CategoryAdmin)
