from django.contrib import admin
from blog.models import Posts, Category

# Register your models here.
class PostClass(admin.ModelAdmin):
    list_display = ('title', 'owner', 'published')


admin.site.register(Posts, PostClass)
admin.site.register(Category)
