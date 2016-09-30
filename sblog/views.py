from django.shortcuts import render
from django.http import Http404

from .models import Blog

# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request,"sblog/blog_list.html",{"blogs":blogs})

def blog_show(request,id):
    try:
        blog = Blog.objects.get(id = id)
    except Blog.DoesNotExist:
        raise Http404
    return render(request,"sblog/blog_show.html",{"blog":blog})