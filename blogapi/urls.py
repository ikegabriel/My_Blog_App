from django.urls import path
from .views import apiview,post_list,post_detail,create_post


urlpatterns = [
    path('',apiview, name='test'),
    path('posts',post_list, name='posts'),
    path('posts/<int:pk>',post_detail, name='post'),
    path('create_post/',create_post, name='create_post'),
]
