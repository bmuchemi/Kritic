from django import forms
from .models import Post, Rating

class uploadForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile', 'created_at']

class rateProject(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']