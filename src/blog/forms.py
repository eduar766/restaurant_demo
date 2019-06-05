from django import forms
from tinymce import TinyMCE
from .models import Blog, Comment

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class CommentForm(forms.ModelForm):
    person = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'E-mail'
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Message'
    }))
    
    class Meta:
        model = Comment
        fields = ('person', 'email', 'content')