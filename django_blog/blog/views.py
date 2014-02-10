from django.shortcuts import render_to_response

from blog.models import Posts

def index(request):
	return render_to_response('blog/index.html', {
		'posts': Posts.objects.all().order_by('-pub_date')
	})

def interna(request):
	return render_to_response('blog/interna.html', {
		'posts': Posts.objects.all().order_by('-pub_date')
	})