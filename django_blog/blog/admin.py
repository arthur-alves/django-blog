# coding: utf-8
from django.contrib import admin
from django import forms
from blog.models import Posts, Category


def make_public(modeladmin, request, queryset):
    queryset.update(published=True)
make_public.short_description = "Publicar"


def make_private(modeladmin, request, queryset):
    queryset.update(published=False)
make_private.short_description = "Não publicar"


class PostClass(admin.ModelAdmin):
    list_display = ('title', 'owner', 'published')
    actions = [make_public, make_private]

    class Media:
        js = ('js/jquery-1.11.0.min.js',
              'js/bootstrap-markdown.js',
              'js/Markdown.Converter.js',
              'js/script.js',
              )
        css = {'all': ('css/bootstrap-markdown.min.css',
                       'css/customAdmin.css',
                       'http://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css',
                       )
               }


admin.site.register(Posts, PostClass)
admin.site.register(Category)
