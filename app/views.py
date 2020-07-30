from django.shortcuts import render,get_object_or_404
from . forms import BookingForm, ContactForm
from django.contrib import messages

# Create your views here.

def home(request):
    
    return render(request,'index.html')

def about(request):
    return  render(request,'about.html')

def booking(request):
    booking_form = BookingForm(request.POST)
    if booking_form.is_valid():
        create_contact = booking_form.save()
        messages.success(request, 'Thank you for booking. you will recieve a confimation call shortly')

    content={
        'booking_form':booking_form,
        
    }
    return  render(request,'booking.html', content)

def contact(request):
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        create_contact = contact_form.save()
        messages.success(request, 'Message sent successfully!!')

    content={
        'contact_form':contact_form,
        
    }
    return  render(request,'contact.html', content)
