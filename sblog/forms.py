#coding:utf-8
from django import forms
from pagedown.widgets import PagedownWidget
from .models import Blog,Tag,Author

class BlogForm(forms.ModelForm):
    caption = forms.CharField(
        required=True,
        widget=PagedownWidget(),
        error_messages={'required':'标题不能为空'},
        label=u'标题',
    )
    content = forms.CharField(
        required=True,
        widget=PagedownWidget(),
        error_messages={'required':'内容不能为空'},
        label=u'内容',
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.order_by('id'),
        required=True,
        error_messages={'required':u'至少选择一个'},
        widget=forms.CheckboxSelectMultiple,
        label=u'标签',
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.order_by('name'),
        required=True,
        error_messages={'required':u'请选择一个'},
        label=u'作者',
    )

    class Meta:
        model = Blog
        fields = '__all__'

    def save(self, inblog, commit=True):
        if inblog:
            blog = inblog
        else:
            blog = Blog()
        blog.caption = self.cleaned_data['caption']
        blog.content = self.cleaned_data['content']
        blog.author = self.cleaned_data['author']
        blog.author.save()
        tags = list(self.cleaned_data['tags'])
        blog.save()
        for item in tags:
            blog.tags.add(item)
        if commit:
            blog.save()
        return blog
"""
class TagForm(forms.ModelForm):
    tag_name = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Tag
        fields = '__all__'

class AuthorForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Author
        fields = '__all__'
"""

