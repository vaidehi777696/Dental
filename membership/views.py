from django.shortcuts import render
from .models import Membership

# Create your views here.
def membership(request):
    membership_info = Membership.objects.first()  # Assuming there's only one Membership instance
    return render(request, 'membership.html', {'membership_info': membership_info})