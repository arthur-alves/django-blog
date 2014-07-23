# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import markdown
from django.core.validators import MaxLengthValidator
from markupfield.fields import MarkupField
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    category = models.CharField(
        u'Categorias', primary_key=True, max_length=255
    )

    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    def __unicode__(self):
        return self.category


class Posts(models.Model):
    owner = models.ForeignKey(
        User, related_name='entries', verbose_name='Criador')
    title = models.CharField(u'Título', max_length=100)
    slug = AutoSlugField(populate_from='title', overwrite=True,
                         max_length=255, editable=False)
    resumo = models.TextField(u'Resumo', validators=[MaxLengthValidator(173)])
    wording = MarkupField(
        default_markup_type='markdown', verbose_name=u'Texto')
    tags = models.CharField(max_length=255)
    category = models.ForeignKey(Category, verbose_name='Categoria')
    pub_date = models.DateTimeField(
        u'Data de Publicação', auto_now_add=True)
    published = models.BooleanField(u'Publicar?', default=False)
    img_post =  models.ImageField(upload_to='post_img')

    class Meta:
        verbose_name = u'Postagem'
        verbose_name_plural = u'Postagens'

    def __unicode__(self):
        return self.title
