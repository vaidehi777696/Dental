from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('email/', views.email_view, name='email_view'),
    path('address/', views.address_view, name='address_view'),

]