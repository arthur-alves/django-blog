# coding: utf-8
from django.contrib import admin
from blog.models import Posts, Category

# Register your models here.


def make_public(modeladmin, request, queryset):
    queryset.update(published=True)
make_public.short_description = "Publicar"


def make_private(modeladmin, request, queryset):
    queryset.update(published=False)
make_private.short_description = "Não publicar"


class PostClass(admin.ModelAdmin):
    list_display = ('title', 'owner', 'published')
    actions = [make_public, make_private]


admin.site.register(Posts, PostClass)
admin.site.register(Category)
