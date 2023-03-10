from django import forms
from django.forms import ModelForm
from . import models

from .models import Article


class PostForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'body', 'img')
        labels = {'title': 'lets give a title', 'body': 'write what you want to', 'img': 'want to upload image...'}