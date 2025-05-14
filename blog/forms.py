from django.forms import ModelForm
from .models import ContentBlog

from django.forms import ModelForm, Textarea, TextInput, Select

class BlogFrom(ModelForm):
    
    class Meta:
        model = ContentBlog
        fields = ('title','image','content','category')
        widgets = {
            'title': TextInput(attrs={'class':'form-control', 'placeholder': 'Title'}),
            'content': Textarea(attrs={'class':'form-control', 'placeholder': 'Content'}),
            'category': Select(attrs={'class':'form-control', 'placeholder': 'Category'})
        }
        