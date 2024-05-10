from django.shortcuts import render
from .models import HomePageContent
# Create your views here.

def home(request):
    # Assuming there's only one instance of HomePageContent
    home_content = HomePageContent.objects.first()
    upcoming_events = home_content.upcoming_events.all()
    office_bearers = home_content.office_bearers.all()
    context = {
        'association_info': home_content.association_info,
        'logo': home_content.logo,
        'college_photo': home_content.college_photo,
        'write_up': home_content.write_up,
        'upcoming_events': upcoming_events,
        'office_bearers': office_bearers,
    }
    return render(request, 'home.html', context)