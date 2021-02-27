from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.views import View
from .models import *

class PostsView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'post/index.html', context= {"posts" : posts})

    def post(self, request):
        text = ""
        for i in request.POST:
            text += f"{i} = {request.POST[i]}\n"

        return HttpResponse("Привет, ты мне передал:\n" + text)

class PostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        # tags = Tag.objects.filter(id__in = post.tags)
        return render(request, 'post/post.html', context= {"post" : post})

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        post.like()
        post.save()
        return render(request, 'post/post.html', context= {"post" : post})

class PostTagView(View):
    def get(self, request, tag):
        tag = Tag.objects.get(name='#'+tag)
        posts = Post.objects.filter(tags=tag)
        return render(request, 'post/index.html', context= {"posts" : posts})
        

class wat(View):
    def get(self, request):
        return render(request, 'post/wat.html')