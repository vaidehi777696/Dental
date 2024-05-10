from django.contrib import admin
from .models import Contact
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_number', 'email', 'address')