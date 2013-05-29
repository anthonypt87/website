from blog.models import Entry
from django.shortcuts import get_object_or_404
from django.shortcuts import render

def index(request):
	latest_entries = Entry.objects.order_by('-time_posted')[:5]
	context = {
		'latest_entries': latest_entries,
	}
	return render(request, 'blog/index.html', context)

def detail(request, entry_id):
	entry = get_object_or_404(Entry, pk=entry_id)
	return render(request, 'blog/detail.html', {'entry': entry})
