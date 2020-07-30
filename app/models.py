from django.db import models

# Create your models here.
LCHOICES = (
    ('feature','Feature'),
    ('studio', 'Studio Session')
)
class Booking(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=100, blank=False)
    booking_type = models.CharField(max_length=100,choices = LCHOICES)
    time = models.CharField(max_length=100,blank=False)
    notes = models.TextField(max_length=2000, blank=True)


    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField(max_length=2000, blank=False)


    def __str__(self):
        return self.name