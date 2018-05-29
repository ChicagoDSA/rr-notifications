from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from accounts.models import WorkingGroup

class MessageType(models.Model):
    ''' 
    Represents the type of message being sent. It is not being used at the momement. 
     '''
    name = models.CharField('Name of the type of message', max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # later on we can add some sort of relationship here to restrict who gets what messages

class Message(models.Model):
    message_text = models.TextField('Message being sent out')
    # optional URL to be appended to be included in the text
    message_url = models.CharField('Link that can be included in message', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



class SentMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    message = models.ForeignKey(Message, on_delete=models.PROTECT)
    # adding the received boolean field now incase we implement webhooks
    # maybe if someone has more the X number of messages fail we remove them from the system
    recevied = models.BooleanField('Did the texting API return success', default=False)
    time_sent = models.DateTimeField(auto_now_add=True)