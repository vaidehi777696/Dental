from django.contrib import admin
from .models import AssociationInfo, OfficeBearer, NewsEvent, HomePageContent

# Register your models here.
@admin.register(AssociationInfo)
class AssociationInfoAdmin(admin.ModelAdmin):
    list_display = ('association_name', 'contact_info')

@admin.register(OfficeBearer)
class OfficeBearerAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')

    def photo_display(self, obj):
        return obj.photo.url if obj.photo else "No photo"


@admin.register(NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date','description')

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('association', 'write_up')

    filter_horizontal = ('office_bearers', 'upcoming_events')

    def write_up(self, obj):
        return obj.write_up[:50] + '...' if obj.write_up else "No write-up"

    write_up.short_description = 'Write-up'