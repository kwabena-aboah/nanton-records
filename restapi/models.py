import string
import random
from django.db import models
from users.models import User
from users.get_usernames import current_request
from .validators import validate_image_extension


class Received(models.Model):
    registry_number = models.CharField(max_length=8, help_text="File Name.")
    to_whom_received = models.CharField(max_length=255, help_text="Receiver of the document")
    date_of_letter = models.DateField(auto_now_add=False)
    reference_number = models.CharField(max_length=255, help_text="Reference number of the document")
    subject = models.TextField()
    remarks = models.CharField(max_length=255, help_text="Short notes on document")
    file_directory = models.FileField(upload_to='received-files/%y-%m-%d/', validators=[validate_image_extension])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_recieved = models.DateField(auto_now_add=False)
    
    class Meta:
        verbose_name = "Received"
        verbose_name_plural = "Received"
    
    def __str__(self):
        return self.registry_number
    
    def save(self, *args, **kwargs):
        # strings = 4
        # randoms = ''.join(random.choices(string.ascii_uppercase + string.digits, k = strings))
        '''Automatically generate registry number'''
        if not self.id:
            self.user = current_request().user
            # self.registry_number = '{randoms}{user:04d}'.format(
            #     user=Received.objects.count(), randoms=str(randoms))
        return super(Received, self).save(*args, **kwargs)
    

class Dispatched(models.Model):
    registry_number = models.CharField(max_length=8, help_text="File Name.")
    to_whom_sent = models.CharField(max_length=255, help_text="Destination of the document")
    date_of_letter = models.DateField(auto_now_add=False)
    reference_number = models.CharField(max_length=255, help_text="Reference number of the document")
    subject = models.TextField()
    remarks = models.CharField(max_length=255, help_text="Short notes on document")
    file_directory = models.FileField(upload_to='dispatched-files/%y-%m-%d/', validators=[validate_image_extension])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_dispatched = models.DateField(auto_now_add=False)
    
    class Meta:
        verbose_name = "Dispatched"
        verbose_name_plural = "Dispatched"
    
    def __str__(self):
        return self.registry_number
    
    def save(self, *args, **kwargs):
        # strings = 4
        # randoms = ''.join(random.choices(string.ascii_uppercase + string.digits, k = strings))
        '''Automatically generate registry number'''
        if not self.id:
            self.user = current_request().user
            # self.registry_number = '{randoms}{user:04d}'.format(
            #     user=Dispatched.objects.count(), randoms=str(randoms))
        return super(Dispatched, self).save(*args, **kwargs)