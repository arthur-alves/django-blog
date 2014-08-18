from django.shortcuts import render_to_response
from django.http import HttpResponse
from blog.models import Posts
from blog.models import Category
import oauth2 as oauth
import json
import os


def index(request):
    return render_to_response('blog/index.html', {
        'posts': Posts.objects.all().order_by('-pub_date').filter(
            published=True
        ),
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
        'listagem': Posts.objects.all().order_by('-pub_date').filter(published=True),
        'categorias': Category.objects.all()
    })


def categorias(request):
    return render_to_response('blog/categorias.html',{
        'todas': Category.objects.all(),
        'categorias': Category.objects.all().reverse(),
        })

def sobre(request):
    return render_to_response('blog/sobre.html')


def hashtags(request):
    # dados do app no Twitter DEV
    API_KEY = os.environ['API_KEY']
    API_SECRET = os.environ['API_SECRET']

    TOKEN = os.environ['TOKEN']
    TOKEN_SECRET = os.environ['TOKEN_SECRET']

    # Login

    #import ipdb; ipdb.set_trace()
    consumer = oauth.Consumer(key=API_KEY, secret=API_SECRET)
    token = oauth.Token(key=TOKEN, secret=TOKEN_SECRET)
    client = oauth.Client(consumer, token)

    search_url = "https://api.twitter.com/1.1/search/tweets.json?q=%23python+%23Python&lang=pt&count=50"

    response, data = client.request(search_url)

    tweets = json.loads(data)

    return HttpResponse(json.dumps(tweets['statuses']), mimetype='application/json')

    # for tweet in tweets['statuses']:
    #     print "Autor: %s" % tweet['user']['name'], tweet['text']
