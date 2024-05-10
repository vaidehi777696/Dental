from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Association model to store association name and contact information
class AssociationInfo(models.Model):
    association_name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.association_name

# OfficeBearer model to store the name and photo of office bearers
class OfficeBearer(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='office_bearers/')

    def __str__(self):
        return self.name

# NewsEvent model to store news and events with title, description, and date
class NewsEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

# HomePageContent model to combine all components needed for the home page
class HomePageContent(models.Model):
    association = models.ForeignKey(AssociationInfo, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos/')
    college_photo = models.ImageField(upload_to='college_photos/')
    write_up = models.TextField()
    office_bearers = models.ManyToManyField(OfficeBearer)
    upcoming_events = models.ManyToManyField(NewsEvent, related_name='upcoming_events')

    def __str__(self):
        return "Home Page Content"