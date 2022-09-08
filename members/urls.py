from django.urls import path
from .views import UserRegisterView,UserUpdateView,PasswordChangeView,LoginView
from django.contrib.auth import views as auth_views # This allows us to use some of the views that come with the django authentication system if needed
from .forms import UserLoginForm

urlpatterns = [
    path('register/',UserRegisterView.as_view(), name='register'),
    path('update_profile/',UserUpdateView.as_view(), name='update_profile'),
    path('password/',PasswordChangeView.as_view(), name='password'),
    path('login/', LoginView.as_view(), name='user_login'),
]