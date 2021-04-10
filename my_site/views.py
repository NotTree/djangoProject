from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db.models import Q

from post.models import *
from post.forms import *
from django.views.generic.detail import DetailView

class Profile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'user-profile.html')

class UserProfile(DetailView):
    model = User # Модель которую хочешь вывести
    template_name = 'user-profile.html' # Путь к html

    def get_context_data(self, **kwargs): # Отвечает за выводимые параметры
        context = super().get_context_data(**kwargs)
        # Чтобы получать объекты ABOBA
        # all
        # get
        # filter
        
        # posts = Post.objects.filter(author__user__id=self.pk)
        # context["posts"] = posts 
        return context
        