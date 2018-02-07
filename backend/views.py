from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import JSONParser

from .models import Post, AutoPost, FurniturePost, ElectronicPost, HousePost, LawnPost, JobAndServicePost
from .models import PhotoURL
from .serializers import PostSerializer, AutoPostSerializer, FurniturePostSerializer
from .serializers import ElectronicPostSerializer, HousePostSerializer, LawnPostSerializer, JobAndServicePostSerializer
from .serializers import PhotoURLSerializer

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

@csrf_exempt
def update_photo_url(request, pk):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PhotoURLSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def update_all(request):
    '''
    Storing the Urls of PHOTOS for a POST passing the Post ID
    '''
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PhotoURLSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)

def get_photo_urls(request, post_id):
    '''
    Getting the urls of PHOTOS for a POST passing the POST ID
    '''
    if request.method == 'GET':
        p = PhotoURL.objects.filter(post_id=post_id)
        ps = PhotoURLSerializer(p, many=True)
        return JsonResponse(ps.data, safe=False)
