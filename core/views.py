from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post, Category
from django.core.paginator import Paginator

def frontpage(request):
    recent_posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')[:5]  # Get 5 most recent posts
    posts = Post.objects.filter(status=Post.ACTIVE)

    recent_paginator = Paginator(recent_posts, 1) 
    paginator = Paginator(posts, 5)

    recent_page_number = request.GET.get('recent_page')
    recent_page_obj = recent_paginator.get_page(recent_page_number)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/frontpage.html', {
        'recent_posts': recent_page_obj,
        'posts': page_obj,
        'page_number': page_number,
        'recent_page_number': recent_page_number,
        'total_pages': paginator.num_pages,
        'total_recent_pages': recent_paginator.num_pages,
    })


def about(request):
    return render(request, 'core/about.html')


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")

