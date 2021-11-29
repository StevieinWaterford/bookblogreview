from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post



class PostList(generic.ListView):
     model = Post
     queryset = Post.objects.filter(status=1).order_by("-created_on")
     template_name = "home.html"

class PostDetail(View):
     def get (self,request, slug, *args, **kwargs):
          queryset = Post.objects.filter(status=1)
          post = get_object_or_404(queryset, slug=slug)
          comments = post.comments.filter(approved = True).order_by("created_on")
          liked = False
          if Post.likes.filter(id=self.request.user.id).exists():
              liked = True

          return render (
             request,
             "post_detail.html",
             {
                 "post": post,
                 "comments" : comments,
                 "liked" : liked
         },
         ) 



     model = Post
     template_name = "blog/post_detail.html"




# class Postlist(generic.Listview):
#     model = Post
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'home.html'
    
