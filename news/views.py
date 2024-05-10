from django.shortcuts import render,redirect
from .models import Event
from datetime import date
# Create your views here.
def upcoming_events(request):
    today = date.today()
    upcoming_events = Event.objects.filter(date__gte=today)
    return render(request, 'upcoming_events.html', {'upcoming_events': upcoming_events})

def past_events(request):
    today = date.today()
    past_events = Event.objects.filter(date__lt=today)
    return render(request, 'past_events.html', {'past_events': past_events})