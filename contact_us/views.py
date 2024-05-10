from django.shortcuts import render
from .models import Contact

# Create your views here.
def contact(request):
    contact_info = Contact.objects.first()  # Assuming there's only one Contact instance
    return render(request, 'contact.html', {'contact_info': contact_info})

def email_view(request):
    contact_info = Contact.objects.first()  # Assuming there's only one Contact instance
    return render(request, 'email.html', {'email': contact_info.email})

def address_view(request):
    contact_info = Contact.objects.first()  # Assuming there's only one Contact instance
    return render(request, 'address.html', {'address': contact_info.address})