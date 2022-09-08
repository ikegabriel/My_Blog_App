from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.urls import reverse_lazy
from .forms import SignUpForm, UserUpdateForm, ChangePasswordForm,UserLoginForm

# Create your views here.
class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')


class UserUpdateView(UpdateView):
    form_class = UserUpdateForm
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    # form_class = PasswordChangeForm
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('update_profile')


class LoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'
    success_url = 'home'

    