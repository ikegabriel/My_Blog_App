from django.urls import path
from . import views

urlpatterns = [
    #path('', BlogHomeView.as_view(), name='home'),
    path('', views.index, name='home'),
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('categories/', views.categories, name='categories'),
    path('category/<str:cats>', views.category, name='category'),
    path('apicall/', views.apicall, name='apicall'),
    path('add_category/', views.CategoryCreateView.as_view(), name='add_category'),
    path('<pk>/detail/', views.BlogDetailView.as_view(), name='detail'),
    path('<pk>/update/', views.BlogUpdateView.as_view(), name='update'),
    path('<pk>/delete/', views.BlogDeleteView.as_view(), name='delete'),
    path('like/<pk>/', views.like, name='post_likes'),
    path('favourite/<pk>/', views.favourite, name='favourite'),
    path('profile/', views.profile, name='profile'),
    path('weather/', views.weather, name ='weather')
]