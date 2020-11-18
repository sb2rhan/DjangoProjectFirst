from django import forms
from django.forms import fields
from posts.models import Post


"""
    This class responsible to form that creates Post models in front-end
"""
class PostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['author'].widget.attrs['class'] = 'form-control'
        self.fields['tag'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = '__all__'
