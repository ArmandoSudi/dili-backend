from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from backend import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^posts/$', views.PostList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
