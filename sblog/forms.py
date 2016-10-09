from django import forms

from pagedown.widgets import PagedownWidget
from .models import Blog,Tag

class BlogForm(forms.ModelForm):
    caption = forms.CharField(widget=PagedownWidget())
    content = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Blog
        fields = '__all__'

class TagForm(forms.ModelForm):
    tag_name = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Tag
        fields = '__all__'

