from django import forms
from phonenumber_field.modelfields import PhoneNumberField
class SignupForm(forms.Form):
    name = forms.CharField(label='Report Name', max_length=100)
    phone_number = PhoneNumberField();

    email = forms.EmailField(label='Recipient Email')
