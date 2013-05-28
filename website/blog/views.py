from blog.models import Entry, Category
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

def index(request):
	latest_entries = Entry.objects.order_by('-time_posted')[:5]
	template = loader.get_template('blog/index.html')
	context = Context({
		'latest_entries': latest_entries,
	})
	return HttpResponse(template.render(context))
#	context = {
#		'categories': Category.objects.all(),
#		'posts': Entry.objects.all()
#	}
#	return render(request, 'blog/index.html', context)

def view_post(request, blog_id):
	return HttpResponse('hi')
