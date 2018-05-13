import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify    
import datetime
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.



class Account(models.Model):
    """Stores information about someone subscribing to the text messages

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # phone numbers MUST be saved in E.164 format, take a gander over on Google to learn more
    phone_number = PhoneNumberField()
    name = models.CharField(_('Member Name'),max_length=255)
    zip_code = models.IntegerField(_('Active Zip Code'))
    opted_in = models.BooleanField('Has this account opted in for texts', default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}-{1}".format(self.name, self.phone_number)


