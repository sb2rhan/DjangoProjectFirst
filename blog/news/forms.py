from django import forms
from django.forms import fields
from news.models import News


class NewsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['theme'].widget.attrs['class'] = 'form-control'
        self.fields['theme'].widget.attrs['placeholder'] = 'Theme'
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['publisher'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = News
        fields = '__all__'
