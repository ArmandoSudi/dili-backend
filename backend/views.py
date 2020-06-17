from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from datetime import datetime
import logging
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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
    return HttpResponse("<h1>Hello from Dili !</h1>")

class PostList(generics.ListCreateAPIView):
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

@csrf_exempt
@api_view(['POST', 'GET'])
def post_list(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            post = serializer.save(publication_date=datetime.now(), thumbnail_url='www.google.com')
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

def get_post(request, category_code):
    """
    Return all the post whose category are child to category_code
    """
    subcategories = Category.objects.filter(parent_category=category_code)
    ids = []
    for category in subcategories:
        ids.append(category.id)

    posts = Post.objects.filter(category__in=ids)
    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['POST', 'PUT'])
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

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES['picture']:
        """
        Uploading the picture first
        """
        myFile = request.FILES[ 'picture']
        
        fs = FileSystemStorage()
        print(myFile.name)
        generagedFileName = fs.generate_filename(myFile.name)
        fileName = fs.save(generagedFileName, myFile)
        print("FILE NAME: " + fileName)
        uploaded_file_url = fs.url(fileName)
        print("FILE URL: " + uploaded_file_url)

        print(request.POST)

        # # Saving the post to DB"

        post = Post()
        post.product_brand = request.POST['product_brand']
        post.product_model = request.POST['product_model']
        post.prodcut_price = int(request.POST['product_price'])
        post.product_description = request.POST['product_description']
        post.category = Category.objects.get(pk=int(request.POST['category_id'])) 
        post.currency = Currency.objects.get(pk=int(request.POST['currency_id']))
        post.publication_date = datetime.now()
        post.thumbnail_url = "http://10.0.2.2:8000" + uploaded_file_url

        post.save()

        return JsonResponse('{"response": "ok"}', status=201, safe=False)
    return JsonResponse('{"response": "could not upload file"}', status=400, safe=False)
    
def get_categories(request, category_code):
    """
    Getting the child category of a parent category of id category_id
    """
    if request.method == 'GET':
        categories = Category.objects.filter(parent_category=category_code)
        categories_serialized = CategorySerializer(categories, many=True)
        return JsonResponse(categories_serialized.data, safe=False)