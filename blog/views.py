from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,\
        DetailView,CreateView,UpdateView,\
        DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from . import models

# Create your views here.


def about(request):
    return render(request, 'blog/about.html')


def home(request):
    posts = models.Post.objects.all()
    return render(request, 'blog/home.html', context={'posts': posts})

class PostListView(ListView):
    model= models.Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model= models.Post
    template_name='blog/post_detail.html'

class PostCreateView(LoginRequiredMixin ,CreateView):
    model=models.Post
    fields=['title','description']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=models.Post
    fields=['title','description']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model= models.Post
    success_url='/'
    
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False