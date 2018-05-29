from django import forms
from .models import Account, WorkingGroup
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class SignupForm(forms.Form):
    phone_number = PhoneNumberField(min_length=10, label="Your Phone Number")
    zip_code = forms.CharField(min_length=5, max_length=5, label="Your Zip Code (blank is fine)")
    working_groups = forms.ModelMultipleChoiceField(
        queryset = WorkingGroup.objects.all(), # not optional, use .all() if unsure
        widget  = forms.CheckboxSelectMultiple,
        label="Current Working Groups you are part of."
    )

    def __init__(self, qs=None, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['working_groups'].queryset = WorkingGroup.objects.filter(active=True)


