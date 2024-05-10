from django.db import models

# Create your models here.
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    ug_batch = models.CharField(max_length=10, blank=True, null=True)
    pg_batch = models.CharField(max_length=10, blank=True, null=True)
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    current_designation = models.CharField(max_length=100)
    member_status = models.CharField(max_length=20, choices=[('Already Member', 'Already Member'), ('New Member', 'New Member')])
    membership_number = models.CharField(max_length=20, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    transaction_number = models.CharField(max_length=100, blank=True, null=True)
    payment_transaction_copy = models.ImageField(upload_to='payment_transactions/', null=True, blank=True)
    payment_bank_details = models.TextField(blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=100, blank=True)

    def generate_verification_token(self):
        token = get_random_string(length=32)
        self.email_verification_token = token
        self.save()
        return token

# models.py

# models.py


class Profile(models.Model):
    username = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    ug_batch = models.CharField(max_length=10, blank=True)
    pg_batch = models.CharField(max_length=10, blank=True)
    current_designation = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True)
    CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
    CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'

class PasswordResetToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)