from django.shortcuts import render_to_response
from django.http import HttpResponse
from twitter_hash import twitter_hash
from blog.models import Posts
from blog.models import Category
import json
import os
import re


def index(request):
    return render_to_response('blog/index.html', {
        'posts': Posts.objects.all().order_by('-pub_date').filter(
            published=True
        ),
        'categorias': Category.objects.all(),
        'tweets': twitter_hash()
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
        'listagem': Posts.objects.all().order_by('-pub_date').filter(published=True),
        'categorias': Category.objects.all()
    })


def categorias(request):
    return render_to_response('blog/categorias.html',{
        'todas': Category.objects.all(),
        'categorias': Category.objects.all().reverse(),
        })

def sobre(request):
    return render_to_response('blog/sobre.html', {
        'categorias': Category.objects.all()
        })


def hashpy(request):
    import ipdb; ipdb.set_trace()
    hashtag = request.COOKIES.get('hash_artpy').replace('#','')
    return render_to_response('blog/hashpy.html', {
        'categorias': Category.objects.all(),
        'tweets': twitter_hash(50, hashtag)
    })

    # for tweet in tweets['statuses']:
    #     print "Autor: %s" % tweet['user']['name'], tweet['text']
