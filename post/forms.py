from django import forms
from .models import *
from django.forms import MultiWidget, TextInput
from django.core.exceptions import ValidationError

class TagForm(forms.Form):
    name = forms.CharField(max_length=128)

class PostForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Указать автора")
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    title = forms.CharField(max_length=128)
    slug = forms.SlugField(max_length=64)
    content = forms.JSONField(max_length=2048)
    publish = forms.ChoiceField(choices=(
        (False, "Не публиковать"),
        (True, "Опубликовать")
    ))

    author.widget.attrs['class'] = "form-control"
    tags.widget.attrs['class'] = "form-control"
    title.widget.attrs['class'] = "form-control"
    slug.widget.attrs['class'] = "form-control"
    content.widget.attrs['class'] = "form-control"
    publish.widget.attrs['class'] = "form-control"

class ModelPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'tags', 'title', 'slug', 'content']

        widgets = { 
            "slug" : forms.TextInput(attrs={'class':"form-control"}),
            "title" : forms.TextInput(attrs={'class':"form-control"}),
            "content" : forms.Textarea(attrs={'cols': 60, 'rows': 25, 'class':"form-control"}),
            "tags" : forms.SelectMultiple(attrs={'class' : 'form-control'}),
            "author" : forms.Select(attrs={'class' : 'form-control'}),
        }

    def clean_slug(self):
        data = self.cleaned_data["slug"]
        if data[0] == '-':
            raise ValidationError("Название не может начинаться не с буквы")
        elif data.lower() == 'null':
            raise ValidationError("Название не может быть null")
        return data

    def clean_title(self):
        data = self.cleaned_data["title"]
        if data[0] == '-':
            raise ValidationError("Название не может начинаться не с буквы")
        elif data.lower() == 'null':
            raise ValidationError("Название не может быть null")
        return data
    

class ModelTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

        widgets = {
            'name' : forms.TextInput(attrs={'class':"form-control"})
        }

    def clean_name(self):
        data = self.cleaned_data["name"]
        if data[0].isalpha():
            raise ValidationError("Название не может начинаться не с буквы")
        elif data.lower() == 'null':
            raise ValidationError("Название не может быть null")
        return data
        