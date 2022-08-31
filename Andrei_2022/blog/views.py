from django.shortcuts import render
from .models import Comment
# Create your views here.


def blog_index(request):
    blogs = Comment.objects.orderby('-created_on')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    blog = Comment.objects.get(pk=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context)
