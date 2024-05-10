from django.shortcuts import render

# Create your views here.
from .models import CustomUser
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetView
from .forms import CustomPasswordResetForm
from .forms import ProfileEditForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page or any other page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def send_verification(user):
    token = user.generate_verification_token()
    verification_link = f'http://example.com/verify-email?token={token}'  # Replace example.com with your domain
    subject = 'Verify Your Email Address'
    html_message = render_to_string('email_verification.html', {'user': user, 'verification_link': verification_link})
    plain_message = strip_tags(html_message)
    from_email = 'your@example.com'  # Replace with your email
    to_email = user.email
    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

def verify_email(request):
    token = request.GET.get('token')
    if token:
        try:
            user = CustomUser.objects.get(email_verification_token=token)
            user.email_verified = True
            user.save()
            return HttpResponse('Email verified successfully!')
        except CustomUser.DoesNotExist:
            return HttpResponse('Invalid verification token.')
    else:
        return HttpResponse('Token parameter is missing.')


def about_us(request):
    return render (request,'about_us.html')
# views.py

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    # Add any other customizations if needed

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})