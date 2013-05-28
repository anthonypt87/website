from django.contrib import admin
from blog import models

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('id', 'title', 'time_posted', 'was_published_recently')
	list_filter = ['time_posted']
	search_fields = ['title', 'id']
	date_hierarchy = 'time_posted'

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Category, CategoryAdmin)
