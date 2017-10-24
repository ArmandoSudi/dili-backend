from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Post, AutoPost, FurniturePost, ElectronicPost, HousePost, LawnPost, JobAndServicePost
from .serializers import PostSerializer, AutoPostSerializer, FurniturePostSerializer
from .serializers import ElectronicPostSerializer, HousePostSerializer, LawnPostSerializer, JobAndServicePostSerializer

def index(request):
    return HttpResponse("Hello from Dili !")

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AutoPostList(generics.ListCreateAPIView):
    queryset = AutoPost.objects.all()
    serializer_class = AutoPostSerializer

class AutoPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AutoPost.objects.all()
    serializer_class = AutoPostSerializer

class FurniturePostList(generics.ListCreateAPIView):
    queryset = FurniturePost.objects.all()
    serializer_class = FurniturePostSerializer

class FurniturePostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FurniturePost.objects.all()
    serializer_class = FurniturePostSerializer

class ElectronicPostList(generics.ListCreateAPIView):
    queryset = ElectronicPost.objects.all()
    serializer_class = ElectronicPostSerializer

class ElectronicPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElectronicPost.objects.all()
    serializer_class = ElectronicPostSerializer

class HousePostList(generics.ListCreateAPIView):
    queryset = HousePost.objects.all()
    serializer_class = HousePostSerializer

class HousePostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HousePost.objects.all()
    serializer_class = HousePostSerializer

class LawnPostList(generics.ListCreateAPIView):
    queryset = LawnPost.objects.all()
    serializer_class = LawnPostSerializer

class LawnPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LawnPost.objects.all()
    serializer_class = LawnPostSerializer

class JobAndServicePostList(generics.ListCreateAPIView):
    queryset = JobAndServicePost.objects.all()
    serializer_class = JobAndServicePostSerializer

class JobAndServicePostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobAndServicePost.objects.all()
    serializer_class = JobAndServicePostSerializer

@api_view(['PUT'])
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
