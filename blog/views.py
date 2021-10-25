from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to my blog!")


def blog_posts(request):
    return HttpResponse("This page will contain all the blog posts!")

def single_blog_post(request, post_name):
    return HttpResponse("This page will contain content of a single post!")