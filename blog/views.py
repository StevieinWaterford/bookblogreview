from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "home.html"

class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post_.html"




# class Postlist(generic.Listview):
#     model = Post
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'home.html'
    
