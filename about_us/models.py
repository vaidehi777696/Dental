from django.db import models

# Create your models here.
# models.py (in your app)
class AboutUs(models.Model):
    write_up = models.TextField()
    # Add other fields as needed

class AboutUsPhoto(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='about_photos/')