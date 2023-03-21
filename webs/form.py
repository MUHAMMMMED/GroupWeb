from django import forms
from webs.models import *      
           
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget      
           
           
           
           
        
class  booking(forms.ModelForm):
 
      
 
      class Meta:
           model = Booking      
           fields = ('name','phone','Doctor', 'knew','Message')      
           exclude = ['STATUS','created_at','web','LandingPage' ]   
      
 
      
class  bookingLandingPage(forms.ModelForm):
 
      class Meta:
           model = Booking      
           fields = ('name','phone','knew','Message')      
           exclude = [ 'LandingPage','STATUS','created_at','web','Doctor']   
      
 
      
      
 
      
 
      
                
#            name = forms.CharField(widget=forms.TextInput(attrs={
#            'class': 'input',
#            'placeholder': 'name'
#            }))
#            Message = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'input',
#         'placeholder': 'Your Message here'
#     }))
 
# # # class  OfersBookingformUpdate(forms.ModelForm):
# # #         required_css_class = 'required'
 
# # #         class Meta:
# # #            model = OffersBooking                   
# # #            fields = "__all__"          
# # #            exclude = ['user','Update_at','guide','price','modern','sample','amount']

# # #            widgets = {
# # #             'date': forms.DateInput( format=('%d/%m/%Y'),   attrs={'class': 'form-control',    'placeholder': 'Select a date', 'type': 'date'  }),     
# # #             'time': forms.DateInput( format=('%H:%M'),   attrs={'class': 'form-control',    'placeholder': 'Select a date', 'type': 'time'  }),  
# # #   }             
 
# # class  OfersBookingformUpdate(forms.ModelForm):
# #         required_css_class = 'required'
 
# #         class Meta:
# #            model = OffersBooking                   
# #            fields = "__all__"          
# #            exclude = ['user','Update_at','guide','price','modern','sample','amount']
 
# #    
           
           
           
           
           
           
           
           
                     
        
#     #        widget=forms.DateTimeInput(attrs={
#     #         'class': 'form-control datetimepicker-input',
#     #         'data-target': '#datetimepicker1'
#     #     })
#     # )  
                    
#                        # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                     
        
#         # def __init__(self, *args, **kwargs):
#         #     super(OffersBooking, self).__init__(*args, **kwargs)    
#         #     for filed_name,field in self.fileds.items():  
#         #         filed.widget.attrs['class']='form-control'
 

#         # date= forms.DateField(            
#         #  label='Data',          
#         #   widget=forms.DateInput(              
#         #     fromat='%Y-%m-%d',    
#         #     attrs={'type':'date',}),
#         #  input_formats=('%Y-%m-%d',),
 
#         #   )    
                   
#         # Update_at= forms.DateTimeField(            
#         #  label='Data/Hore',          
#         #  widget=forms.DateTimeInput(               
#         #    fromat='%Y-%m-%dT-%H:%M',    
#         #    attrs={  'type':'datetime-local',}),
#         #  input_formats=('%Y-%m-%dT-%H:%M',),
 
#         #   )       
#         # time= forms.TimeField( widget= forms.TimeInput( fromat='%H:%M',attrs={ 'type':'datetime-local',}),input_formats=('%H:%M',)    ),                   
         
                   
          
           
         
 
        
  
 
       
       
#         # fields = ('offers','phone','Message','Introduction','knew','Summary','CallToAction','tag','city','country','status')
#         # fields = ('tag','description' )'created_at',
#         # exclude = ['user']
 

#     # description = forms.CharField(widget=forms.Textarea(attrs={
#     #     'class': 'form-control',
#     #     'placeholder': 'What can we help you?',
#     #      'name':'Heading'
#     #      }))
# # class  OfersBookingformUser(forms.ModelForm):
    
# #     class Meta:
# #         model = OffersBooking
# #         fields = ('name','phone','Message')     
# #         name = forms.CharField(widget=forms.TextInput(attrs={
# #         'class': 'form-control',
# #         'placeholder': 'name'
# #     }))
# #     Message = forms.CharField(widget=forms.Textarea(attrs={
# #         'class': 'form-control',
# #         'placeholder': 'Your Message here'
# #     }))
 