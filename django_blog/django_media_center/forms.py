# encoding: utf-8
from django import forms
from .models import ImageUp


class ImageForm(forms.ModelForm):
    title_img = forms.CharField(label="teste", max_length=5, min_length=2, required=False)

    class Meta:
        model = ImageUp
