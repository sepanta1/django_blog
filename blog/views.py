from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
post = [{
    'author': 'nigga',
    'title': 'Blogpost'
}]


def home(request):
    return render(request, 'blog/home.html', context={'post': post})
