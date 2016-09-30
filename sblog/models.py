#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(u'标签',max_length=20,blank=True)
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)

    def __unicode__(self):
        return  self.tag_name

class Author(models.Model):
    """docstring for Author"""
    name = models.CharField(u'姓名',max_length=30)
    email = models.EmailField(u'电子邮箱',blank=True)
    website = models.URLField(u'网址',blank=True)

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    """docstring for Blogs"""
    caption = models.CharField(u'标题',max_length=50)
    author = models.ForeignKey(Author,verbose_name=u"作者")
    tags = models.ManyToManyField(Tag,blank=True,verbose_name=u'标签')
    content = models.TextField(u'内容')
    publish_time = models.DateTimeField(u'发布时间',auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True)

    def __unicode__(self):
        return u'%s %s %s %s' % (self.caption,self.author,self.publish_time,self.tags)

    def tags_names(self):
        return ','.join([a.tag_name for a in self.tags.all()])