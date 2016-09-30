#coding:utf-8
from django.contrib import admin

from sblog.models import Author,Tag,Blog

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('name','email','website')
    search_fields = ('name',)

class BlogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('caption','id','tags_names','author','publish_time')
    list_filter = ('publish_time','author')
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name','create_time')

admin.site.register(Author,AuthorAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Tag,TagAdmin)