from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS =((0,"DRAFT"), (1, "PUBLISHED"))

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

    

# # class Genre(models.Model):
#     genre = models.CharField(max_length = 200)
#     description = models.TextField()

# class Book(models.Model):
#     title = models.CharField(max_length = 200)
#     content = models.TextField()
#     author = models.ForeignKey(Author , on_delete=models.CASCASDE)
#     category = models.ForeignKey(Genre, on_delete=models.CASCADE)


