from django import forms
from .models import Account, WorkingGroup
from phonenumber_field.modelfields import PhoneNumberField
class SignupForm(forms.Form):
    phone_number = PhoneNumberField();
    working_groups = forms.ModelChoiceField(queryset=None)

    def __init__(self, qs=None, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['working_groups'].queryset = WorkingGroup.objects.filter(active=True)


class AccountForm(forms.ModelForm):
    """Form definition for Account."""

    class Meta:
        """Meta definition for Accountform."""

        model = Account
        fields = ('phone_number', 'zip_code',)

