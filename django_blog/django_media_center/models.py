from django.db import models


class ImageUp(models.Model):
    title_img = models.CharField(u'Titulo', max_length=100)
    image = models.ImageField(upload_to='post_img/')

    class Meta:
        verbose_name = u'Imagem'
        verbose_name_plural = u'Imagens'

    def __unicode__(self):
        return self.title_img
