from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Posts
from .serializers import PostSerializer

# Create your views here.
@api_view(['GET'])
def apiview(request):
    api_urls = {
        'List': '/task-list',
        'Detail': '/task-detail/<str:pk>'
    }
    return Response(api_urls['List'])


@api_view(['GET'])
def post_list(request):
    posts = Posts.objects.all()
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_detail(request, pk):
    posts = Posts.objects.get(id=pk)
    serializer = PostSerializer(posts,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)