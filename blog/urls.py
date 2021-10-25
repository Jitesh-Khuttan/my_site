from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('posts', views.blog_posts, name="all-posts"),
    path('posts/<slug:post_name>', views.single_blog_post, name="single-post")
]
