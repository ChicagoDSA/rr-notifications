import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify    
import datetime
# Create your models here.

class Account(models.Model):
    """Stores information about someone subscribing to the text messages

    """
    name = models.CharField(_('Member Name'),max_length=255)
    phone_number = models.CharField(_('Phone NUmnber'), max_length=20)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}-{1}".format(self.name, self.phone_number)


    def save(self, *args, **kwargs):
        d = datetime.datetime.now()
        time = "{0}{1}{2}".format(d.minute, d.seconds, d.microseconds)
        self.slug = slugify("{0}-{1}".format(self.name, time))
        super(ReportResult, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} | {1}".format(self.name, self.report_type)

    def __unicode__(self):
        return "{0} | {1}".format(self.name, self.report_type)

