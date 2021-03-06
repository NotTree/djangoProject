from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.views import View
from .models import *
from django.db.models import Q

class PostsView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'post/index.html', context= {"posts" : posts})

    def post(self, request):
        # print(request)      # выводит объект
        # print(dir(request)) # все свойства и методы
        # print(request.POST)
        # print(request.POST.get('author', ''))
        # posts = Post.objects.filter(author__user__username__iexact=request.POST.get('author', '')) #filter
        posts = Post.objects.filter(
                Q(author__user__username__icontains=request.POST.get('search', '')) |
                Q(tags__name__icontains=request.POST.get('search', ''))
            ) #filter
        return render(request, 'post/index.html', context= {"posts" : posts})

class PostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        tags = post.tags.all()
        return render(request, 'post/post.html', context= {"post" : post, 'tags' : tags})

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        tags = post.tags.all()
        post.like()
        post.save()
        return render(request, 'post/post.html', context= {"post" : post, 'tags' : tags})

class PostTagView(View):
    def get(self, request, tag):
        tag = Tag.objects.get(name='#'+tag)
        posts = Post.objects.filter(tags=tag)
        tags = post.tags.all()
        return render(request, 'post/index.html', context= {"posts" : posts, 'tags' : tags})

class PostAuthorView(View):
    def get(self, request, author):
        posts = Post.objects.filter(author__user__username=author)
        return render(request, 'post/index.html', context= {"posts" : posts})

class wat(View):
    def get(self, request):
        return render(request, 'post/wat.html')
    
    def post(self, request):
        print(request.POST)
        return render(request, 'post/wat.html')
