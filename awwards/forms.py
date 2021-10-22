from .models import Profile
from django import forms

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username','bio','avatar']
