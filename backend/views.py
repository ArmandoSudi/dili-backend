from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer

def index(request):
    return HttpResponse("Hello from Dili !")

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
