from django.shortcuts import render,redirect
from django.http import Http404

from .models import Blog,Tag,Author
from .forms import BlogForm,TagForm

# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()
    tags = Tag.objects.all()
    return render(request,"sblog/blog_list.html",{"blogs":blogs,"tags":tags})

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
    return  render(request,"sblog/blog_filter.html",{"blogs":blogs,"tag":tag,"tags":tags})

def blog_add(request,id=""):
    if request.method == "POST":
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)

        if form.is_valid() and tag.is_valid():
            cd = form.cleaned_data
            cdtag = tag.cleaned_data
            tagname = cdtag['tag_name']
            for taglist in tagname.split():
                Tag.objects.get_or_create(tag_name = taglist.strip())
            title = cd['caption']
            author = Author.objects.get(id=id)
            content = cd['content']
            blog = Blog(caption=title,author=author,content=content)
            for taglist in taglist.split():
                blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                blog.save()
            id = Blog.objects.order_by('-publish_time')[0].id
            return redirect("/sblog/blog/%s" % id)
    else:
        form = BlogForm()
        tag = TagForm(initial={'tag_name':'notags'})
    return render(request,"sblog/blog_add.html",{'form':form,'tag':tag})

def blog_update(request,id=""):
    id = id
    if request.method == "POST":
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            cd = form.cleaned_data
            cdtag = tag.cleaned_data
            tagname = cdtag['tag_name']
            tagnamelist = tagname.split()
            for tag in tagnamelist:
                Tag.objects.get_or_create(tag_name=tag.strip())
            title = cd['caption']
            content = cd['content']
            blog = Blog.objects.get(id=id)
            if blog:
                blog.caption = title
                blog.content = content
                blog.save()
                for tag in tagnamelist:
                    blog.tags.add(Tag.objects.get(tag_name=tag.strip()))
                    blog.save()
                tags = blog.tags.all()
                for tag in tags:
                    tag = str(tag)
                    if tag not in tagnamelist:
                        notag = blog.tags.get(tag_name=tag)
                        blog.tags.remove(notag)
            else:
                blog = Blog(caption=title,content=content)
                for tag in tagnamelist:
                    blog.tags.add(Tag.objects.get(tag_name=tag.strip()))
                    blog.save()
            return redirect('/sblog/blog/%s' % id)
    else:
        try:
            blog = Blog.objects.get(id=id)
        except Exception:
            raise Http404
        form = BlogForm(initial={'caption':blog.caption,'content':blog.content},auto_id=False)
        tags = blog.tags.all()
        if tags:
            taginit = ""
            for x in tags:
                taginit += str(x)+' '
            tag = TagForm(initial={'tag_name':taginit})
        else:
            tag = TagForm()
    return render(request,"sblog/blog_add.html",{'blog':blog,'form':form,'tag':tag})
