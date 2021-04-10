from django import forms
from .models import *
from django.forms import MultiWidget, TextInput
from django.core.exceptions import ValidationError
from django.utils.text import slugify

def create_slug(text:str):
    new_slug = ""
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъьэюя'
    for al in alf():
        for s in slugify(text, True):
            if s == 'а':
                new_slug += 'a'
            elif s == 'б':
                new_slug += 'b'
            elif s[-1] == 'ы':
                new_slug += 's'
            elif s == al[2]:
                new_slug += 'v'
            elif s == al[3]:
                new_slug += 'g'
            elif s == al[4]:
                new_slug += 'd'
            elif s == al[5]:
                new_slug += 'e'
            elif s == al[6]:
                new_slug += 'eyo'
            elif s == al[7]:
                new_slug += 'zh'
            elif s == 'ы':
                new_slug += 'i' 
            elif s == al[8]:
                new_slug += 'z'
            elif s == ' ':
                new_slug += ' '
            elif s == '-':
                new_slug += '-'
            elif s == al[9]:
                new_slug += 'i'
            elif s == al[10]:
                new_slug += "i'"
            elif s == al[11]:
                new_slug += 'k'
            elif s == al[12]:
                new_slug += 'l'
            elif s == al[13]:
                new_slug += 'm'
            elif s == al[14]:
                new_slug += 'n'
            elif s == al[15]:
                new_slug += 'o'
            elif s == al[16]:
                new_slug += 'p'
            elif s == al[17]:
                new_slug += 'r'
            elif s == al[18]:
                new_slug += 's'
            elif s == al[19]:
                new_slug += 't'
            elif s == al[20]:
                new_slug += 'u'
            elif s == al[21]:
                new_slug += 'f'
            elif s == al[22]:
                new_slug += 'h'
            elif s == al[23]:
                new_slug += 'ts'
            elif s == al[24]:
                new_slug += 'ch'
            elif s == al[25]:
                new_slug += 'sh'
            elif s == al[26]:
                new_slug += "sh'"
            elif s == al[27]:
                new_slug += "'"
            elif s == al[28]:
                new_slug += "'"
            elif s == al[29]:
                new_slug += 'e'
            elif s == al[30]:
                new_slug += 'iu'
            elif s == al[31]:
                new_slug += 'ya'

        
            
        
               # ...privet mainers 

class TagForm(forms.Form):
    name = forms.CharField(max_length=128)

class PostForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Указать автора")
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    title = forms.CharField(max_length=128)
    slug = forms.SlugField(max_length=64)    #.create_slug
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
        fields = ['tags', 'title', 'slug', 'content'] # 'author'

        widgets = { 
            "slug" : forms.TextInput(attrs={'class':"form-control"}),
            "title" : forms.TextInput(attrs={'class':"form-control"}),
            "content" : forms.Textarea(attrs={'cols': 60, 'rows': 25, 'class':"form-control"}),
            "tags" : forms.SelectMultiple(attrs={'class' : 'form-control'}),
            # "author" : forms.Select(attrs={'class' : 'form-control'}),
        }
   
    def clean_slug(self):
        data = self.cleaned_data["slug"]
        if data.lower() == 'null':
            raise ValidationError("Название не может быть null")
        return slugify(data, True)

    def clean_title(self):
        data = self.cleaned_data["title"]
        if data[0] in ['null', '-', '.', ',', '!', '?', '%', '#', '*', '@', '$', '^', ':', '(', ')']:         #  $  @ * ^
            raise ValidationError("Название не может начинаться не с буквы")
        return data

#   -------   # 

class ModelTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

        widgets = {
            'name' : forms.TextInput(attrs={'class':"form-control"})
        }
    def clean_name(self):
        data = self.cleaned_data["name"]
        if data.lower() == 'null':
            raise ValidationError("Название не может быть null")
        return slugify(data, True)
