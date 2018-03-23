from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import JSONParser

from .models import Post, AutoPost, FurniturePost, ElectronicPost, HousePost, LawnPost, JobAndServicePost
from .models import PhotoURL, MobilePost
from .serializers import PostSerializer, AutoPostSerializer, FurniturePostSerializer
from .serializers import ElectronicPostSerializer, HousePostSerializer, LawnPostSerializer, JobAndServicePostSerializer
from .serializers import PhotoURLSerializer, MobilePostSerializer

# Get an instance of a logger
logger = logging.getLogger(__name__)

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

class MobilePostList(generics.ListCreateAPIView):
    queryset = MobilePost.objects.all()
    serializer_class = MobilePostSerializer

class MobilePostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MobilePost.objects.all()
    serializer_class = MobilePostSerializer

class AutoPostList(generics.ListCreateAPIView):
    queryset = AutoPost.objects.all()
    serializer_class = AutoPostSerializer

class AutoPostDetail(generics.RetrieveUpdateDestroyAPIView):
    logger.info("hihihihihi")
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

class PhotoURLList(generics.ListCreateAPIView):
    queryset = PhotoURL.objects.all()
    serializer_class = PhotoURLSerializer

# def set_thumbnail(post_id, thumbnail_url):
#     post = Post.objects.all().get(pk=post_id)
#     post.thumbail = photoUrl.url
#     post.save();

@api_view(['POST'])
def post_photo(request, category_code):
    """
    Post a PHOTO URL for that POST, make it a thumbnail if it is a thumbnail
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PhotoURLSerializer(data=data)
        if serializer.is_valid():
            photoUrl = serializer.save()
            set_thumbnail(photoUrl.post_id, int(category_code), photoUrl.url)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def set_thumbnail(post_id, category_code, thumbnail_url):
    if category_code == 0: # mobile category
        mobilePost = MobilePost.objects.get(pk=post_id)
        mobilePost.set_thumbnail_url(thumbnail_url)

    elif category_code == 1: # Electronic category
        pass

    elif category_code == 2: # Car category
        autoPost = AutoPost.objects.get(pk=post_id)
        autoPost.set_thumbnail_url(thumbnail_url)

    elif category_code == 3: # Furniture category
        pass

    elif category_code == 4: # Fashion category
        pass

    elif category_code == 5: # Real Estate category
        housePost = HousePost.objects.get(pk=post_id)
        housePost.set_thumbnail_url(thumbnail_url)

    elif category_code == 6: # Jobs and services category
        pass

    elif category_code == 7: # Show Category
        pass

@api_view(['PUT'])
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

def get_photo_urls(request, post_id, category_code):
    '''
    Getting the urls of PHOTOS for a POST passing the POST ID
    '''
    if request.method == 'GET':
        p = PhotoURL.objects.filter(post_id=post_id, category_code=category_code)
        ps = PhotoURLSerializer(p, many=True)
        return JsonResponse(ps.data, safe=False)
