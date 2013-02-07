from blog.models import Blog, Category
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context = {
		'categories': Category.objects.all(),
		'posts': Blog.objects.all()
	}
	return render(request, 'blog/index.html', context)

def view_post(request, blug_id):
	return HttpResponse('hi')
