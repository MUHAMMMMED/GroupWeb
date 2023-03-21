from django.contrib import admin
from django.urls import path
from  webs.views  import *

from django.conf.urls.static import static
from django.conf import settings
app_name='webs'
urlpatterns = [
 path('',home, name="home"),  
#  path('Bookinsg',Booking,name="booking"),
#  path('success',Bookingsuccess, name="BookingSuccess"),
#  path('Guide/<str:slug>',servicesdetailsGuide, name="Guide"),
 path('<str:slug>',web, name="web"),
 path('offer/<str:slug>',landingpage, name="landingpage"),
 path('doctor/<str:slug>',doctor, name="doctoR"),
 
 
 
 
 ] 
 
 