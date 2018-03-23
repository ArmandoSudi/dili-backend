from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from backend import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^update_post/(?P<pk>[0-9]+)/$', views.PostUpdate.as_view()),
    url(r'^update/(?P<pk>[0-9]+)/$$', views.update_post),

    # posting image for a post
    url(r'^post/photo/(?P<category_code>[0-9]+)/$', views.post_photo, name='post_photo_url'),
    url(r'^post/photos/$', views.update_all, name='post_photo_urls'),
    url(r'^get/photos/(?P<post_id>[0-9]+)/(?P<category_code>[0-9]+)/$', views.get_photo_urls, name='get_photo_url'),

    # mobile and tablette Posts
    url(r'^mobile_posts/$', views.MobilePostList.as_view()),
    url(r'^mobile_post/(?P<pk>[0-9]+)/$', views.MobilePostDetail.as_view()),

    # auto post urls
    url(r'^auto_posts/$', views.AutoPostList.as_view()),
    url(r'^auto_post/(?P<pk>[0-9]+)/$', views.AutoPostDetail.as_view()),

    # furniture post urls
    url(r'^furniture_posts/$', views.FurniturePostList.as_view()),
    url(r'^furniture_post/(?P<pk>[0-9]+)/$', views.FurniturePostDetail.as_view()),

    # electronic post urls
    url(r'^electronic_posts/$', views.ElectronicPostList.as_view()),
    url(r'^electronic_post/(?P<pk>[0-9]+)/$', views.ElectronicPostDetail.as_view()),

    #house post urls
    url(r'^house_posts/$', views.HousePostList.as_view()),
    url(r'^house_post/(?P<pk>[0-9]+)/$', views.HousePostDetail.as_view()),

    # lawn post urls
    url(r'^lawn_posts/$', views.LawnPostList.as_view()),
    url(r'^lawn_post/(?P<pk>[0-9]+)/$', views.LawnPostDetail.as_view()),

    # job and service post urls
    url(r'^job_and_service_posts/$', views.JobAndServicePostList.as_view()),
    url(r'^job_and_servicep_post/(?P<pk>[0-9]+)/$', views.JobAndServicePostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
