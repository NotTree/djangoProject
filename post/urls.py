from django.urls import path, include

from .views import *
# http://127.0.0.1:8000/ wat/

# 200 - все ок
# 300 - перенаправление ahmet/228 --> ohmed/003
# 400 - ошибка клиента
# 500 - сервера

urlpatterns = [
    path('', PostsView.as_view(), name="post_api_url"),
    path('tag/<str:tag>/', PostTagView.as_view(), name="postTags"),
    path('author/<str:author>/', PostAuthorView.as_view(), name="postAuthor"),
    path('create-<str:model>/', Controller.as_view(), name='controller'),
    path('post/<slug:slug>/', PostView.as_view(), name="view"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="detailView")
]