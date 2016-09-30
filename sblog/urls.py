from django.conf.urls import url
from django.contrib import admin

from sblog import views as sblog_views

admin.autodiscover()

urlpatterns = [
    url(r'^bloglist/',sblog_views.blog_list,name='bloglist'),
    url(r'^blog/(?P<id>\d+)/$',sblog_views.blog_show,name = "detailblog"),
    url(r'^blog/(?P<id>\w+)/del/$',sblog_views.blog_del,name="delblog"),
    url(r'^blog/tag/(?P<id>\d+)/$',sblog_views.blog_filter,name="filterblog"),
    url(r'^blog/add/$',sblog_views.blog_add,name="addblog"),
]