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
    # phone numbers MUST be saved in E.164 format, take a gander over on Google to learn more
    phone_number = PhoneNumberField()
    name = models.CharField(_('Member Name'),max_length=255)
    zip_code = models.CharField(_('Active Zip Code'), max_length=10)
    opted_in = models.BooleanField('Account opted out of texts', default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}-{1}".format(self.name, self.phone_number)



class WorkingGroup(models.Model):
    """ 
    Represents a working group. Has a ManyTomany Reltionship with Account
    Intermediate table (pivot table?) is created automaitcally by DJango as far as I know
    """
    name = models.CharField(max_length=255)
    accounts = models.ManyToManyField(Account, 'members', blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('name',)
