from django.urls import path
from . import views

urlpatterns = [
    path('membership/', views.membership, name='membership'),
    # Add other membership-related URLs here
]