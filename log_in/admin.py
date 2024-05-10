from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser, Profile, PasswordResetToken

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'mobile_number', 'member_status', 'email_verified']
    search_fields = ['username', 'email', 'mobile_number']
    list_filter = ['member_status', 'email_verified']

admin.site.register(CustomUser, CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'ug_batch', 'pg_batch', 'current_designation']
    search_fields = ['username__username', 'ug_batch', 'pg_batch', 'current_designation']

admin.site.register(Profile, ProfileAdmin)

class PasswordResetTokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'token', 'created_at']
    search_fields = ['user__username', 'token']
    list_filter = ['created_at']

admin.site.register(PasswordResetToken, PasswordResetTokenAdmin)




# Register your models here.