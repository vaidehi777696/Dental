# forms.py
from django import forms
from .models import AboutUs, AboutUsPhoto

class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['text_content']

class AboutUsPhotoForm(forms.ModelForm):
    class Meta:
        model = AboutUsPhoto
        fields = ['photo']