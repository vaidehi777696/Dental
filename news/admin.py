from django.contrib import admin
from .models import Event

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'is_past_event']
    list_filter = ['date', 'is_past_event']
    search_fields = ['title', 'description']
    date_hierarchy = 'date'