from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('posts/', views.PostView.as_view(), name= 'posts_list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail),
]