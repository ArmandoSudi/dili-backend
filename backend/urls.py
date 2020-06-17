from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from backend import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^posts/(?P<category_code>[0-9]+)/$', views.get_post),
    url(r'test/$', views.post_list),
    url(r'upload_image/$', views.upload_file),
    url(r'^update_post/(?P<pk>[0-9]+)/$', views.PostUpdate.as_view()),
    url(r'^update/(?P<pk>[0-9]+)/$$', views.update_post),
    url(r'^my_posts/(?P<user_uid>[\w-]+)/$', views.get_my_posts),

    url(r'^categories/$', views.CategoryList.as_view()),
    url(r'^categories/child_categories/(?P<category_code>[0-9]+)/$', views.get_categories),

    # posting image for a post
    url(r'^post/photo/(?P<category_code>[0-9]+)/$', views.post_photo, name='post_photo_url'),
    url(r'^post/photos/$', views.update_all, name='post_photo_urls'),
    url(r'^get/photos/(?P<post_id>[0-9]+)/(?P<category_code>[0-9]+)/$', views.get_photo_urls, name='get_photo_url'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
