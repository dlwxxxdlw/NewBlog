from django.shortcuts import render,redirect
from django.http import Http404

from .models import Blog,Tag,Author
from .forms import BlogForm

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

def blog_filter(request,id=""):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id = id)
    blogs = tag.blog_set.all()
    return  render(request,"sblog/blog_filter.html",{"blogs":blogs,"tag":tag,"tags":tag})

def blog_add(request,id=""):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd['caption']
            author = Author.objects.get(id=id)
            content = cd['content']
            blog = Blog(caption=title,author=author,content=content)
            blog.save()
            id = Blog.objects.order_by('-publish_time')[0].id
            return redirect("/sblog/blog/%s" % id)
    else:
        form = BlogForm()
    return render(request,"sblog/blog_add.html",{'form':form})