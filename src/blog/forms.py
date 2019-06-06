from django import forms
from tinymce import TinyMCE
from .models import Blog, Comment

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={
                'required':False,
            }
        )
    )

    class Meta:
        model = Blog
        fields = ('title', 'content', 'thumbnail', 'is_video', 'video_url', 'category', 'tag',)

class CommentForm(forms.ModelForm):
    person = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name'
            }))
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'E-mail'
            }))
    com = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Message'
            }))

    class Meta:
        model = Comment
        fields = ('person', 'email', 'com')
