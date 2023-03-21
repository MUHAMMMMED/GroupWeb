from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(WEB)
admin.site.register(Questions) 
admin.site.register(Image) 
admin.site.register(Insurance) 

admin.site.register(Doctors)

admin.site.register(Section) 

admin.site.register(LandingPage) 
admin.site.register(LandingPageDescription) 
admin.site.register(LandingPageImage) 
admin.site.register(LandingPageBeforeAfter) 
admin.site.register(LandingPageReviews) 
admin.site.register(LandingPageQuestions) 
admin.site.register(LandingPagePrice) 













@admin.register(Booking)
class BookingAdmin(ImportExportModelAdmin):

    model = Booking
    model = Booking
    list_display = ['created_at','name' , 'phone','Message','web','LandingPage', 'Doctor','knew' ]
    list_filter = ( 'created_at','name' , 'phone','Message','web','LandingPage', 'Doctor','knew' )
 