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
import json

from .models import Category, Currency, UserType, User, Post, Location 
from .models import PhotoURL
from .serializers import PostSerializer, CategorySerializer
from .serializers import PhotoURLSerializer

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

class PhotoURLList(generics.ListCreateAPIView):
    queryset = PhotoURL.objects.all()
    serializer_class = PhotoURLSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

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

def get_my_posts(request, user_uid):

    if request.method == "GET":
        auto_posts = AutoPost.objects.filter(user_uid=user_uid)
        mobile_posts = MobilePost.objects.filter(user_uid=user_uid)
        house_posts = HousePost.objects.filter(user_uid=user_uid)

        post_summary = []

        for auto_post in auto_posts:
            post_summary.append(PostSummary(post_id=auto_post.id, name=auto_post.brand, price=auto_post.price, category_code=2))

        for mobile_post in mobile_posts:
            post_summary.append(PostSummary(post_id=mobile_post.id, name=mobile_post.brand, price=mobile_post.price, category_code=6))

        for house_post in house_posts:
            post_summary.append(PostSummary(post_id=house_post.id, name=house_post.address, price=house_post.price, category_code=5))

        my_posts = PostSummarySerializer(post_summary, many=True)

    return JsonResponse(my_posts.data, safe=False)