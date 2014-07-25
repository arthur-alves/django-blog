from django.shortcuts import render_to_response
from blog.models import Posts
from blog.models import Category


def index(request):
    return render_to_response('blog/index.html', {
        'posts': Posts.objects.all().order_by('-pub_date').filter(
            published=True
        ),
        'carrousel': Posts.objects.all().order_by('-pub_date').filter(
            published=True
        )[:3],
        'categorias': Category.objects.all()
    })


def interna(request, slug):
    return render_to_response('blog/interna.html', {
        'article': Posts.objects.get(slug=slug),
        'categorias': Category.objects.all()
    })


def listagem(request, category):
    return render_to_response('blog/listagem.html', {
        'listagem': Posts.objects.all().filter(category=category,
                                               published=True),
        'categorias': Category.objects.all()
    })


def listagem_geral(request):
    return render_to_response('blog/listagem.html', {
        'listagem': Posts.objects.all().filter(published=True),
        'categorias': Category.objects.all()
    })

def sobre(request):
    return render_to_response('blog/sobre.html')