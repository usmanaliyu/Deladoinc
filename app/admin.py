from django.contrib import admin
from . models import Booking, Contact

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','booking_type','time')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject')
admin.site.register(Booking,BookingAdmin)
admin.site.register(Contact,ContactAdmin)