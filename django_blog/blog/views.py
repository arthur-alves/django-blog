from django.shortcuts import render_to_response
from blog.models import Posts


def index(request):
    return render_to_response('blog/index.html', {
        'posts': Posts.objects.all().order_by('-pub_date').filter(
            published=True
        ),
        'carrousel': Posts.objects.all().order_by('-pub_date').filter(
            published=True
        )[:3]
    })


def interna(request, slug):
    return render_to_response('blog/interna.html', {
        'article': Posts.objects.get(slug=slug)
    })
