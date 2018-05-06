from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(label='Report Name', max_length=100)
    email = forms.EmailField(label='Recipient Email')
