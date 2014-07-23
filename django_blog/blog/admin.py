# coding: utf-8
from django.contrib import admin
from django import forms
from blog.models import Posts, Category
import os


def make_public(modeladmin, request, queryset):
    queryset.update(published=True)
make_public.short_description = "Publicar"


def make_private(modeladmin, request, queryset):
    queryset.update(published=False)
make_private.short_description = "Não publicar"


class PostClass(admin.ModelAdmin):
    list_display = ('title', 'owner', 'published')
    list_filter = ('title', 'owner')
    readonly_fields = ('wording_markup_type',)
    actions = [make_public, make_private]
    exclude = ('owner',)
    # fieldsets = (
    #         (None, {
    #             'fields' : ('title', 'owner', 'published')
    #             }),
    #         ('Opções Avançadas', {
    #             'classes' : ('collapse',),
    #             'fields' : ('tags', 'resumo', 'wording')
    #             }),
    #     )

    def save_model(self, request, obj, form, change):
        # import ipdb; ipdb.set_trace()
        obj.owner = request.user
        obj.save()

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


class CategoryClass(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.category = obj.category.lower()
        obj.save()

admin.site.register(Posts, PostClass)
admin.site.register(Category, CategoryClass)
