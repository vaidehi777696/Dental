from django.db import models

# Create your models here.
class Membership(models.Model):
    process_to_become_member = models.TextField()
    bank_details = models.TextField()
    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return "Membership Information"