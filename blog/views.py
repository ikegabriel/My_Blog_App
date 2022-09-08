from django.shortcuts import redirect, render, get_object_or_404
from .models import Posts,Category
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import BlogForm, BlogUpdateForm
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
# =====================================
import json
import urllib.request

# Create your views here.
class BlogHomeView(ListView):
    model = Posts
    fields = '__all__'
    template_name = 'home.html'
    ordering = ['-date'] # This is one way to order your template data, ascending or descending order. You can also use id etc.

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'create_category.html'
    success_url = '/categories'

def categories(request):
    category_load = Category.objects.all()
    data = {
        'category': category_load
    }
    return render(request, 'categories.html', data,)

def like(request, pk):
    if request.POST.get('action') == 'post':
        result = ''
        liked = False
        post = get_object_or_404(Posts, id=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            result = post.total_likes()
            post.save()
        else:
            post.likes.add(request.user)
            result = post.total_likes()
            post.save()
            liked = True
    return JsonResponse({'result':result})
def weather(request):
    if request.POST.get('action') == 'post':
        # city = request.POST.get['city']
        result = {}
        print(request.POST)
        try:
            city = request.POST.get('city')
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city + f'&units=metric&appid=0e1791a71ccff9f26ec1de019ec1b1e8').read()

            list_of_data = json.loads(source)

            data = {
                'country_code': str(list_of_data['sys']['country']),
                'temp': str(list_of_data['main']['temp']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': str(list_of_data['weather'][0]['icon'])
            }
        except:
            data = {}
    else:
        data = {}
    print(data)
    return JsonResponse({'result':data})

    
def favourite(request, pk):
    if request.method == 'POST':
        fav = ''
        post = get_object_or_404(Posts, id=pk)
        if post.favourites.filter(id=request.user.id).exists():
            post.favourites.remove(request.user)
            post.save()
            fav = False
        else:
            post.favourites.add(request.user)
            post.save()
            fav = True
    return JsonResponse({'fav':fav})


def category(request, cats):
    category = Posts.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'category.html',{'cats':cats.replace('-', ' ').upper,'category':category})

'''def profile(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        profile_details = Posts.objects.all()
        
        return render(request, 'profile.html', profile_details)'''

class BlogCreateView(CreateView):
    model = Posts
    form_class = BlogForm
    template_name = 'create.html'
    #fields = '__all__'
    #success_url = '/' we can use success url in place of get_absolute_url.

class BlogListView(ListView):
    model = Posts
    fields = '__all__'
    template_name = 'list.html'

class BlogDetailView(DetailView):
    model = Posts
    fields = '__all__'
    template_name = 'detail.html'

    
# To display the Post likes on the detail view
    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        collect_post_likes = get_object_or_404(Posts, id=self.kwargs['pk'])
        collect_favs = Posts.objects.all().order_by('-favourites')
        # This verifies if a user has liked or unliked a post and returns the total likes to the view
        liked = False
        disliked = False
        if collect_post_likes.likes.filter(id=self.request.user.id).exists():
            liked = True
        
            
        total_likes = collect_post_likes.total_likes()

        context['total_likes'] = total_likes
        context['liked'] = liked
        context['favs'] = collect_favs
        return context

class BlogUpdateView(UpdateView):
    model = Posts
    form_class =  BlogUpdateForm
    # fields = [
    #     'title',
    #     'title_tag',
    #     'article',
    #     'article_snippet',
    # ]
    template_name = 'update.html'
    #success_url = '/'

class BlogDeleteView(DeleteView):
    model = Posts
    template_name = 'delete.html'
    success_url = '/'

def profile(request):
    return render(request, 'profile.html', {})

# class ProfileUpdateView(UpdateView):
    
#     template_name = 'profile_update.html'
#     # queryset = 
#     fields = [
#         'bio',
#         'profile_picture',
#         'twitter',
#         'facebook',
#         'instagram',
#         'website'
#     ]
#     def get_object(self):
#         user = self.request.user
#         return Profile.objects.get(user=user)


def apicall(request):
    import requests

    response = requests.get('http://127.0.0.1:8000/api/posts')
    ans = response.json()
    data = {
        'data': ans
    }
    return render(request, 'apicall.html',data)

def index(request, *args):
    posts = Posts.objects.all().order_by('-date')
    data = {
        'object_list': posts
    }

    return render(request, 'home.html', data)


def trending(request):
    data ={
        'a':'Nothing Here'
    }
    return render(request, 'home.html', data)