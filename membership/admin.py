from django.contrib import admin
from .models import Membership
# Register your models here.
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_person')