from django.shortcuts import render
from .models import Post
from django.http import Http404

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    try:
        post = Post.objects.get(slug=post, publish__year=year, publish__month=month, publish__day=day)
    except Post.DoesNotExist:
        raise Http404('Not Found')
    
    return render(request, 'blog/post/detail.html', {'post': post})
   