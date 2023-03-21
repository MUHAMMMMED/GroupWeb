from django.shortcuts import render, redirect
from webs.models import *
import pandas as pd
from webs.form import *
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home(request):
    wEB =WEB.objects.filter(active=True)
    doctor =Doctors.objects.filter(active=True)
    landingpage =LandingPage.objects.filter(active=True)
    context = {
   
        'web':wEB,
        'landingpage':landingpage,
        'doctor':doctor
    
    } 
    return render(request, 'home2.html', context) 


 
def web(request, slug):
 
    WeB = get_object_or_404(WEB,slug=slug)

    if request.method=='POST':
        form= booking(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)    
            myform.web=WeB 
            myform.save()

            print('DOne')  
            context = {
            'form':form,
              'WEb':WeB}
 
 
            return render(request, 'WEb.html', context)
    else:
        form = booking()
        print('404')  
 
    context = {
   
       'WEb':WeB,
       'form':form,
    
    } 
    return render(request, 'WEb.html', context)

def landingpage(request, slug):
    landingPage = get_object_or_404(LandingPage,slug=slug)
    data =LandingPage.objects.filter(slug=landingPage).values() 
    print(data )
    data_df = pd.DataFrame(data)
    data_web=data_df["WebName"] 
    print(data_web )
    data_web1=data_web.tolist()
    print(data_web1 )
    data_web2=data_web1[0]
    print(data_web2 )
    if request.method=='POST':
        form= bookingLandingPage(request.POST)
        if form.is_valid():
           myform = form.save(commit=False)    
           myform.LandingPage=landingPage 
           myform.web=data_web2 
           myform.save()

           print('DOne')  
        #    context = {
        #     'form':form,
        #       'landingPage':landingPage}
        #    return render(request, 'offer.html', context)
    else:
        form = bookingLandingPage()
        print('404') 
 
    context = {
   'form':form,
       'landingPage':landingPage
 
    
    } 
 
    return render(request, 'offer.html', context)

 
def doctor(request, slug):
    doctoR = get_object_or_404(Doctors,slug=slug)
    # if request.method=='POST':
    #     form= booking(request.POST)

    #     if form.is_valid():
    #         myform = form.save(commit=False)
    #         myform.price=PriceServicesdetails
    #         form.save()

    #         print('DOne')      
    #         return redirect ('Services:BookingSuccess') 
    # else:
    #     form = booking()
 
 
    context = {
   
       'doctor':doctoR,
    #    'form':form
    
    } 
 
    return render(request, 'doctor.html', context)

















# def Booking(request):   
#     if request.method=='POST':
#         Bookingform= booking(request.POST)

#         if Bookingform.is_valid():
#             myform = Bookingform.save(commit=False)
#             myform.save() 
#             return redirect ('Services:BookingSuccess') 
#     else:
#         Bookingform = booking()
 
 
#     context = {
   
  
#        'Bookingform':Bookingform
#         } 
 
#     return render(request, 'ContactUs.html', context)   
# def Bookingsuccess(request):
#     servicesGuide =Guide.objects.filter(active=True)
#     servicesModern =Modern.objects.filter(active=True)
#     servicesSample =Sample.objects.filter(active=True) 
#     servicesPrice =Price.objects.filter(active=True)    
    
   
#     context = {  
#      'servicesGuide':servicesGuide ,
#      'servicesModern':servicesModern,    
#      'servicesSample':servicesSample,   
#      'servicesPrice':servicesPrice, } 

#     return render(request, 'servicessuccess.html', context) 
   
 
 
         
    
 