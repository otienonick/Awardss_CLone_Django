from .models import Profile,Post
from django import forms

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username','bio','avatar']

class PostModelForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3} ))
    location = forms.CharField(label = 'Your location')

    class Meta:
        model = Post
        fields = ['project_name','description','url','image','location',]           
