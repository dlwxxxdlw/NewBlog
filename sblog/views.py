from django.shortcuts import render,redirect
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

def blog_del(request,id=""):
    try:
        blog = Blog.objects.get(id = id)
    except Exception:
        raise Http404
    if blog:
        blog.delete()
        return  redirect("/sblog/bloglist/")
    blogs = Blog.objects.all()
    return render(request,"sblog/blog_list.html",{"blogs":blogs})