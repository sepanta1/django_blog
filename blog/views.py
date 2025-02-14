from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.


def home(request):
    posts = models.Post.objects.all()
    return render(request, 'blog/home.html', context={'posts': posts})
