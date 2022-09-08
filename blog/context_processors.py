from .models import Posts

def popular(request):
    return{'favourites': Posts.objects.all().order_by('-favourites')}