from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return "Contact Information"