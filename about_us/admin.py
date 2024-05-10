from django.contrib import admin
# Register your models here.
from django import forms
from .models import AboutUs,AboutUsPhoto

admin.site.register(AboutUs)
admin.site.register(AboutUsPhoto)