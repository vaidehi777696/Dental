from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import PasswordResetForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'mobile_number', 'address', 'ug_batch', 'pg_batch', 'photo', 'current_designation', 'member_status', 'membership_number', 'payment_date', 'transaction_number', 'payment_transaction_copy', 'payment_bank_details']



class CustomPasswordResetForm(PasswordResetForm):
    # Add any custom fields or logic if needed
    pass


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'ug_batch', 'pg_batch', 'photo' , 'current_designation']  # Specify the fields you want to include in the form