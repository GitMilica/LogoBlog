from django.shortcuts import render
from datetime import date
from .models import Post


def get_date(post):
    return post['date']

# Create your views here.

def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all_posts.html', {
        "all_posts": all_posts 
    })

def post_detail(request, slug):
    
    identified_post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {
        "post": identified_post
    })