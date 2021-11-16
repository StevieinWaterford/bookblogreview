from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS =((0,"DRAFT"), (1, "PUBLISHED"))

class textEditor(models.Model): 

   content = models.TextField()

class Post(models.Model):
    name = models.CharField(max_length = 200, unique=True)
    slug = models.CharField(max_length = 200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)

class Meta:
    ordering = ['-created_on']

    def _str_(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80, unique=True)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    actions = ['approved_comments']

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


    

    

# # class Genre(models.Model):
#     genre = models.CharField(max_length = 200)
#     description = models.TextField()

# class Book(models.Model):
#     title = models.CharField(max_length = 200)
#     content = models.TextField()
#     author = models.ForeignKey(Author , on_delete=models.CASCASDE)
#     category = models.ForeignKey(Genre, on_delete=models.CASCADE)


