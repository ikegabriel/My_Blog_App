from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User

# Try to use custom user form to avoid all this hassle
'''
I hid the label text with css
'''
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    first_name = forms.CharField(label='', max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter First Name'}))
    last_name = forms.CharField(label='', max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Last Name'}))
    username = forms.CharField(label='', max_length=250)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter Password Again'


class UserUpdateForm(UserChangeForm):
    first_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control'}))
    #last_login = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form_control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # is_superuser = forms.CharField(max_length=250, widget=forms.CheckboxInput(attrs={'class':'form_check'}))
    # is_staff = forms.CharField(max_length=250, widget=forms.CheckboxInput(attrs={'class':'form_check'}))
    # is_active = forms.CharField(max_length=250, widget=forms.CheckboxInput(attrs={'class':'form_check'}))
    #date_joined = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form_control'}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        )

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = (
            'old_password',
            'new_password1',
            'new_password2',
        )

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', max_length=250)
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label= '', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(label= '', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter password',
        }
))
