from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

class LikeMixin:
    def like(self):
        self.likes += 1
        if self.likes % 10 == 0 and self.priopity < 100:
            self.priopity += 1                                  #1000 лайков до максимума  ❤999 == 100 priority 
    
    def dislike(self):
        self.likes -= 1
        if self.likes+1 % 10 == 0 and self.priopity > 0:
            self.priopity -= 1

class Author(LikeMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    priopity = models.PositiveIntegerField(default=2, validators=(MaxValueValidator(100.0), ))
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

class Tag(LikeMixin, models.Model):
    name = models.TextField(max_length=128, blank=False, unique=True)
    priopity = models.PositiveIntegerField(default=2, validators=(MaxValueValidator(100.0), ))
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Post(LikeMixin, models.Model): 
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    title = models.TextField(max_length=128, blank=False)
    slug = models.SlugField(max_length=128, unique=True)
    content = models.TextField(max_length=4096, blank=False)
    priopity = models.PositiveIntegerField(default=2, validators=(MaxValueValidator(100.0), ))
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title