from django.shortcuts import render_to_response

from blog.models import Posts


def index(request):
    return render_to_response('blog/index.html', {
        'posts': Posts.objects.all().order_by('-pub_date')
    })


def interna(request, slug):
    return render_to_response('blog/interna.html', {
        'article': Posts.objects.get(slug=slug)
    })
