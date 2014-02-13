from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import ImageForm
from django.http import HttpResponseRedirect


def upload_img(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')  # Redirect after POST
    else:
        form = ImageForm()  # An unbound form

    return render(request, 'blog/form.html', {
        'form': form,
    })
