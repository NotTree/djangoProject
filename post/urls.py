from django.urls import path, include

from .views import *
# http://127.0.0.1:8000/ wat/

# 200 - все ок
# 300 - перенаправление ahmet/228 --> ohmed/003
# 400 - ошибка клиента
# 500 - сервера

urlpatterns = [
    path('', PostsView.as_view(), name="post_api_url"),
    path('wat/', wat.as_view()),
    path('tag/<str:tag>/', PostTagView.as_view()),
    path('author/<str:author>/', PostAuthorView.as_view()),
    path('<str:slug>/', PostView.as_view()),
]    