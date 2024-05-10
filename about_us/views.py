from django.shortcuts import render,redirect
from .models import AboutUs

# Create your views here.
def about(request):
    about_instance = AboutUs.objects.first()  # Assuming there's only one AboutUs instance
    photos = about_instance.photos.all() if about_instance else []
    return render(request, 'about.html', {'about': about_instance, 'photos': photos})

