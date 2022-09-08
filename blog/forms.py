
from django import forms
from .models import Posts




class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Posts

        fields = (
            'title',
            'title_tag',
            'header_image',
            'author',
            'category',
            'article',
            'article_snippet',
            'tags',
        )
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'author','type':'hidden'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'article': forms.Textarea(attrs={'class': 'form-control'}),
            'article_snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BlogUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Posts

        fields = (
            'title',
            'title_tag',
            'header_image',
            'category',
            'article',
            'article_snippet',
            'tags',
        )
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'article': forms.Textarea(attrs={'class': 'form-control'}),
            'article_snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This Snippet will be be the displayed on the Home Page'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }
