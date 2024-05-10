from django.db import models

# Create your models here.
# models.py

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    photo = models.ImageField(upload_to='event_photos/')
    is_past_event = models.BooleanField(default=False)

    def __str__(self):
        return self.title