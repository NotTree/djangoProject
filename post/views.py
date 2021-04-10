from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
# Create your views here.
from django.http.response import HttpResponse
from django.views import View
from django.db.models import Q
from django.db.models.functions import Coalesce
from .models import *
from .forms import *


# get - возвращает 1 элемент
# all - возвращает все
# filter - возвращает все подходящие

class PostsView(View):
    def get(self, request):
        posts = None
        if request.GET.get('tag', False) and request.GET.get('author', False):
            posts = Post.objects.filter(
                tags__name__iexact=request.GET['tag'],
                author__user__username__iexact=request.GET['author']
            )
        elif request.GET.get('tag', False):
            posts = Post.objects.filter(tags__name__icontains=request.GET['tag'])
        elif request.GET.get('author', False):
            posts = Post.objects.filter(author__user__username__icontains=request.GET['author'])
        elif request.GET.get('search', False):
            posts = Post.objects.filter(
                Q(author__user__username__icontains=request.GET['search']) |
                Q(tags__name__icontains=request.GET['search'])
            )
        else:
            posts = Post.objects.all()
        
        posts = posts.order_by('likes').reverse()
        return render(request, 'post/index.html', context= {"posts" : posts})

class PostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        tags = post.tags.all()
        comments = Comment.objects.filter(post=post)
        return render(request, 'post/post.html', context= {"post" : post, 
            'tags' : tags, 'comments' : comments})

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        tags = post.tags.all()
        post.like()
        post.save()
        comments = Comment.objects.filter(post=post)
        return render(request, 'post/post.html', context= {"post" : post, 
            'tags' : tags, 'comments' : comments})

class PostDetailView(DetailView): # Импортируй класс DetailView
    model = Post
    template_name = 'templates/logged_out.html'
    
    def get_context_data(self, **kwargs): # Отвечает за выводимые параметры
        context = super().get_context_data(**kwargs)
        return context

class Controller(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    Models = {
        'tag': ModelTagForm,
        'post': ModelPostForm
    }

    def get(self, request, model):
        form = self.Models[model]()
        return render(request, 'post/create_form.html', context={"form" : form})

    def post(self, request, model):
        print(request.POST)
        form = self.Models[model](request.POST)
        if form.is_valid():
            print(request.user)
            if model == 'tag':
                form.save()
            elif model == 'post':
                print(form.cleaned_data)
                data = form.cleaned_data
                author = Author.objects.get(user=request.user)
                post = Post.objects.create(title=data['title'],
                    content=data['content'], slug=data['slug'], author=author)
                for tag in data['tags']:
                    post.tags.add(tag)
                post.save()

        return render(request, 'post/create_form.html', context={"form" : form}) 


#####################################################################################################################
class PostTagView(View):
    def get(self, request, tag):
        tag = Tag.objects.get(name='#'+tag)
        posts = Post.objects.filter(tags__name=tag)
        return render(request, 'post/index.html', context= {"posts" : posts})

class PostAuthorView(View):
    def get(self, request, author):
        posts = Post.objects.filter(author__user__username=author)
        return render(request, 'post/index.html', context= {"posts" : posts})
