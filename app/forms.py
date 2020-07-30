from django import forms
from .models import Booking, Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']
        widgets = {

        }
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','email','phone_number','booking_type','time','notes']

