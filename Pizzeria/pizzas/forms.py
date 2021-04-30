from django import forms
from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["description"]
        labels = {"description": "What would you like to say?"}
