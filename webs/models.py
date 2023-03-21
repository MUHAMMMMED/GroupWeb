from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
 
# Create your models here.

class Doctors(models.Model):  

   slug = models.CharField(max_length = 50 , unique = True )  
   active = models.BooleanField(default = False) 
   Image = models.FileField(upload_to = "files/images/Doctors/photos/%Y/%m/%d/",blank=True, null=True)
   Name = models.CharField(max_length = 300 ,blank=True, null=True)
   jobtitle= models.CharField(max_length = 300 ,blank=True, null=True)
   Description= models.CharField(max_length = 300 ,blank=True, null=True)
#    AppreciationCertificateImage = models.FileField(upload_to = "files/images")
#    Experience = models.CharField(max_length = 300 , null = True)
#    email = models.CharField(max_length = 50 , null = False )
#    Phone = models.CharField(max_length = 50 , null = False)
#    Address = models.CharField(max_length = 50 , null = False) 
#    University = models.CharField(max_length=100)
#    UniversityIFO= models.CharField(max_length = 300 , null = True)
#    date = models.CharField(max_length=100)
# #    def save(self,*args, **kwargs):
#         self.slug = slugify(self.Name)
#         super(Doctors,self).save(*args, **kwargs)

   def __str__(self):
        return self.Name
  
 
 

# Property models here.

class ServicesProperty(models.Model):
   created_at = models.DateTimeField(auto_now_add=True)
   active = models.BooleanField(default = False)
 
   WebName =models.CharField(max_length=50,blank=True, null=True)
   slug = models.CharField(max_length = 50 , unique = True,blank=True, null=True)
   homepagelink = models.CharField(max_length = 500 ,blank=True, null=True)
   Image = models.FileField(upload_to = "files/images/LandingPage/photos/Image/%Y/%m/%d/",blank=True, null=True)

   ImageName = models.CharField(max_length = 300 ,blank=True, null=True)
   slideImage = models.FileField(upload_to = "files/images/LandingPage/photos/slideImage/%Y/%m/%d/",blank=True, null=True)
   slideImage1 = models.FileField(upload_to = "files/images/LandingPage/photos/slideImage1/%Y/%m/%d/",blank=True, null=True)
   slideImage2 = models.FileField(upload_to = "files/images/LandingPage/photos/slideImage2/%Y/%m/%d/",blank=True, null=True)
   Title = models.CharField(max_length=100)
   Description = models.CharField(max_length = 500 ,blank=True, null=True)
   price = models.CharField(max_length=100,blank=True, null=True)
   discount= models.CharField(max_length=100,blank=True, null=True)
   Doctor = models.ManyToManyField(Doctors,blank=True, null=True)

#    def save(self,*args, **kwargs):
#         self.slug = slugify(self.Titel)
#         super(ServicesProperty,self).save(*args, **kwargs)

   def __str__(self):
        return self.Title
class LandingPageBeforeAfter(models.Model):

    Title = models.CharField(max_length=100,blank=True, null=True)
    Description = models.CharField(max_length = 500 ,blank=True, null=True)
    Image = models.FileField(upload_to = "files/images/LandingPageBeforeAfter/photos/Image/%Y/%m/%d/",blank=True, null=True)
    def __str__(self):
         return self.Title
class LandingPagePrice(models.Model):

    Title = models.CharField(max_length=100,blank=True, null=True)
    def __str__(self):
         return self.Title
class LandingPageQuestions(models.Model):
    question= models.CharField(max_length = 300 ,blank=True, null=True)
    answer = models.CharField(max_length=300,blank=True, null=True)
    def __str__(self):
         return self.question

class LandingPageImage(models.Model):
     Image = models.FileField(upload_to = "files/images/LandingPageImage/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Name = models.CharField(max_length=100,blank=True, null=True)
     def __str__(self):
          return self.Name

class LandingPageReviews(models.Model):
     Image = models.FileField(upload_to = "files/images/LandingPageReviews/photos/Image/%Y/%m/%d/",blank=True, null=True)
     Name = models.CharField(max_length=100,blank=True, null=True)
     def __str__(self):
        return self.Name
class LandingPageDescription(models.Model):
      Titel = models.CharField(max_length=100,blank=True, null=True)
      Description= models.CharField(max_length = 500 ,blank=True, null=True)
      def __str__(self):
         return self.Titel
 # LandingPage models here.
class LandingPage(ServicesProperty):    
     PricePage = models.ManyToManyField(LandingPagePrice,blank=True, null=True)    
     QuestionsPage = models.ManyToManyField(LandingPageQuestions,blank=True, null=True)  
     imagePage = models.ManyToManyField(LandingPageImage,blank=True, null=True)
     ReviewsPage = models.ManyToManyField(LandingPageReviews,blank=True, null=True)
     DescriptionPage = models.ManyToManyField(LandingPageDescription,blank=True, null=True)
     BeforeAfterPage = models.ManyToManyField(LandingPageBeforeAfter,blank=True, null=True)


class WEB(models.Model):
    active = models.BooleanField(default = False)
    slug = models.CharField(max_length = 50 , unique = True,blank=True, null=True)
    FaviconIco= models.FileField(upload_to = "files/images/WEB/photos/FaviconIco/%Y/%m/%d/",blank=True, null=True)
    logo = models.FileField(upload_to = "files/images/WEB/photos/logo/%Y/%m/%d/",blank=True, null=True)
    keywords= models.CharField(max_length = 300,blank=True, null=True)
    authorLinke= models.CharField(max_length = 300 ,blank=True, null=True)
    Title = models.CharField(max_length=100,blank=True, null=True)
    Image = models.FileField(upload_to = "files/images/WEB/photos/Image/%Y/%m/%d/",blank=True, null=True)
    silderImage = models.FileField(upload_to = "files/images/WEB/photos/silderImage/%Y/%m/%d/",blank=True, null=True)
    info = models.CharField(max_length = 300 ,blank=True, null=True)
    Description= models.CharField(max_length = 300 ,blank=True, null=True)
    PHONE = models.CharField(max_length = 300 ,blank=True, null=True)
    Whatsapp= models.CharField(max_length=500,blank=True, null=True)
    linkedinlinke= models.CharField(max_length=500,blank=True, null=True)
    snapchat= models.CharField(max_length=500,blank=True, null=True)
    instagramlinke= models.CharField(max_length=500,blank=True, null=True)
    Twitterlinke= models.CharField(max_length=500,blank=True, null=True)
    facebooklinke= models.CharField(max_length=500,blank=True, null=True)

    OpeningHours= models.CharField(max_length=500,blank=True, null=True)
    Address= models.CharField(max_length=500,blank=True, null=True)    

    Doctor = models.ManyToManyField(Doctors,blank=True, null=True)
    Landingpage = models.ManyToManyField(LandingPage,blank=True, null=True)
 
    def __str__(self):
         return self.Title

class Questions(models.Model):
 
    WEBQuestions = models.ForeignKey(WEB, related_name='qestions', on_delete=models.CASCADE)
    question= models.CharField(max_length = 300 ,blank=True, null=True)
    answer = models.CharField(max_length=300,blank=True, null=True)
    def __str__(self):
         return self.question


class Image(models.Model):
 
   WEBImage = models.ForeignKey(WEB, related_name='image', on_delete=models.CASCADE)
   image = models.FileField(upload_to = "files/images/Image/photos/Image/%Y/%m/%d/",blank=True, null=True)
   imagename = models.CharField(max_length = 300 ,blank=True, null=True)

   def __str__(self):
         return self.imagename

class Insurance(models.Model):
 
   InsuranceImage = models.ForeignKey(WEB, related_name='insurance', on_delete=models.CASCADE)
   name = models.CharField(max_length = 300 ,blank=True, null=True)
   def __str__(self):
         return self.name
class Section(models.Model):
 
   SectioN = models.ForeignKey(WEB, related_name='section', on_delete=models.CASCADE)
   name = models.CharField(max_length = 300 ,blank=True, null=True)
   image = models.FileField(upload_to = "files/images/Section/photos/Image/%Y/%m/%d/",blank=True, null=True)
   Description= models.CharField(max_length = 300 ,blank=True, null=True)

   def __str__(self):
         return self.name

# class INTRODUCING(models.Model):
#     Image = models.FileField(upload_to = "files/images")
#     Titel = models.CharField(max_length=100)
#     DescriptionTop = models.CharField(max_length = 300 , null = True)
#     DescriptionPoint1 = models.CharField(max_length = 300 , null = True)
#     DescriptionPoint2 = models.CharField(max_length = 300 , null = True)
#     DescriptionPoint3 = models.CharField(max_length = 300 , null = True)
#     DescriptionPoint4 = models.CharField(max_length = 300 , null = True)
#     DescriptionPoint5 = models.CharField(max_length = 300 , null = True)
#     DescriptionBottom = models.CharField(max_length = 300 , null = True)
#     button_name= models.CharField(max_length=500)
#     button_link= models.CharField(max_length=500)  

   #  def __str__(self):
   #       return self.Titel



# class Information(models.Model):
#    Copyright = models.CharField(max_length = 300 , null = True) 
#    PHONE = models.CharField(max_length = 300 , null = True) 
#    Twitterlinke= models.CharField(max_length=500)
#    instagramlinke= models.CharField(max_length=500)
#    facebooklinke= models.CharField(max_length=500)
#    Youtubelinke= models.CharField(max_length=500)
#    linkedinlinke= models.CharField(max_length=500)
#    Whatsapp= models.CharField(max_length=500)  
#    Address= models.CharField(max_length=500) 
#    OpeningHours= models.CharField(max_length=500)  
#    def __str__(self):
#          return self.Copyright

# class OpeningHours(models.Model):
#    Titel= models.CharField(max_length = 300 , null = True)
#    def __str__(self):
#          return self.Titel


# class WebsitesINF(models.Model): 
#    LOGO = models.FileField(upload_to = "files/images")
#    FaviconIco= models.FileField(upload_to = "files/images")
#    Titel= models.CharField(max_length = 300 , null = True)
#    Description= models.CharField(max_length = 300 , null = True)
#    keywords= models.CharField(max_length = 300 , null = True)
#    authorLinke= models.CharField(max_length = 300 , null = True)
#    def __str__(self):
#          return self.Titel

 







# from django.db import models
# from django.utils.text import slugify
# # Create your models here.
# class Doctors(models.Model):   
#    Image = models.FileField(upload_to = "files/images")
#    Name = models.CharField(max_length = 300 , null = True)
#    jobtitle= models.CharField(max_length = 300 , null = True)
#    Description= models.CharField(max_length = 300 , null = True)
#    AppreciationCertificateImage = models.FileField(upload_to = "files/images")
#    Experience = models.CharField(max_length = 300 , null = True)
#    email = models.CharField(max_length = 50 , null = False )
#    Phone = models.CharField(max_length = 50 , null = False)
#    Address = models.CharField(max_length = 50 , null = False) 
#    University = models.CharField(max_length=100)
#    UniversityIFO= models.CharField(max_length = 300 , null = True)
#    date = models.CharField(max_length=100)
# #    def save(self,*args, **kwargs):
# #         self.slug = slugify(self.Name)
# #         super(Doctors,self).save(*args, **kwargs)

#    def __str__(self):
#         return self.Name
  

# class Skills(models.Model):
 
#     doctorSkill = models.ForeignKey(Doctors, related_name='doctor', on_delete=models.CASCADE)
#     Skill= models.CharField(max_length = 300 , null = True)
#     percentage = models.CharField(max_length=100)
 


# class Awards(models.Model):
 
#     doctorAwards = models.ForeignKey(Doctors, related_name='doctors', on_delete=models.CASCADE)
#     Award= models.CharField(max_length = 300 , null = True)
#     Description= models.CharField(max_length = 300 , null = True)


# class ReviewsProperty(models.Model):
#      Image = models.FileField(upload_to = "files/images")
#      Name = models.CharField(max_length=100)
 
# class DescriptionnumberProperty(models.Model):
#       number = models.CharField(max_length=100)
#       Titel = models.CharField(max_length=100)
#       Description= models.CharField(max_length = 300 , null = True)
 
# class DescriptionImageProperty(models.Model):
#     Image = models.FileField(upload_to = "files/images")
#     Titel = models.CharField(max_length=100)
#     Description= models.CharField(max_length = 300 , null = True)
 
# class DescriptionpriceProperty(models.Model):
#     Titel = models.CharField(max_length=100)
#     price = models.CharField(max_length=100)
#     Description= models.CharField(max_length = 300 , null = True)
 
# class BeforeAfterProperty(models.Model):
#     BeforeImage = models.FileField(upload_to = "files/images")
#     AfterImage = models.FileField(upload_to = "files/images") 
#     name = models.CharField(max_length = 300 , null = True) 

# class BeforeAfterONEProperty(models.Model):
#     Image = models.FileField(upload_to = "files/images") 
#     name= models.CharField(max_length = 300 , null = True) 

#     slideImage2 = models.FileField(upload_to = "files/images")
#     slideImage3 = models.FileField(upload_to = "files/images")
 
# # Guide models here.
# class Guide(ServicesProperty):   
#    slideImage2 = models.FileField(upload_to = "files/images")
#    slideImage3 = models.FileField(upload_to = "files/images") 
#    doctorname=  models.CharField(max_length=100) 
#    jobtitle= models.CharField(max_length = 300 , null = True)
#    doctorInf= models.CharField(max_length = 300 , null = True)
#    doctorImage = models.FileField(upload_to = "files/images")
#    Price = models.FileField(upload_to = "files/images")

# class GuideReviews(ReviewsProperty):
#     ServicesReviews = models.ForeignKey(Guide, related_name='reviews', on_delete=models.CASCADE)
#     def __str__(self):
#        return self.ServicesReviews
# class  GuideDescriptionNumber(DescriptionnumberProperty):
#     servicesdescription = models.ForeignKey(Guide, related_name='description1', on_delete=models.CASCADE)
#     def __str__(self):
#        return self.servicesdescription
# class GuideDescriptionImage(DescriptionImageProperty):
#     servicesdescription = models.ForeignKey(Guide, related_name='description2', on_delete=models.CASCADE)
#     def __str__(self):
#        return self.servicesdescription
# class GuideBeforeAfter(BeforeAfterProperty):
#     beforeafterImage = models.ForeignKey(Guide, related_name='beforeafter2', on_delete=models.CASCADE)
#     def __str__(self):
#        return self.beforeafterImage

# # Price models here.
# class Price(ServicesProperty):  
#      pass
 
# #    def __str__(self):
# #         return self.Titel

# class PriceDescription(DescriptionpriceProperty):
#     servicesdescription = models.ForeignKey(Price, related_name='description', on_delete=models.CASCADE)
#     def __str__(self):
#        return self.servicesdescription

# class PriceReviews(ReviewsProperty):
#     ServicesReviews = models.ForeignKey(Price, related_name='reviews', on_delete=models.CASCADE)

# class PriceBeforeAfter(BeforeAfterONEProperty):
#     beforeafterImage = models.ForeignKey(Price, related_name='beforeafter', on_delete=models.CASCADE)
#     def __str__(self):
#        return self.beforeafterImage
 


# class ModernDescription(DescriptionnumberProperty):
#     servicesdescription = models.ForeignKey(Modern, related_name='description', on_delete=models.CASCADE)
#     def __str__(self):
#        return self.servicesdescription
# class ReviewsModern(ReviewsProperty):
#     ServicesReviews = models.ForeignKey(Modern, related_name='reviews', on_delete=models.CASCADE)

# class ModernBeforeAfter(BeforeAfterProperty):
#     beforeafterImage = models.ForeignKey(Modern, related_name='beforeafter', on_delete=models.CASCADE)
#     def __str__(self):
#        return self.beforeafterImage
# # Sample models here.
# class Sample(ServicesProperty): 
#          pass
 
# class SamplsDescription(DescriptionpriceProperty):
#     servicesdescription = models.ForeignKey(Sample, related_name='description1', on_delete=models.CASCADE)
#     def __str__(self):
#        return self.servicesdescription
 

 
class Booking(models.Model):
 
    Undefined="كيف عرفتنا"
    insurance='تأمين'
    Friend='صديق '   
    family='أسرة'
    neighbors='الجيران'
    Google='جوجل '  
    Whatsapp ='واتساب'
    snapchat='سناب' 
    Instagram='انستقرام'
    Twitter='تويتر'    
    Facebook='فيس بوك '
    ticktock='تيك توك'
    YouTube='يوتيوب ' 
    Email='البريد الإلكتروني'  
    Site='موقع'  
    other='آخر'

    CHOICES_knew = (
    (Undefined,"كيف عرفتنا"),
    (insurance,'تأمين'),
    (Friend,'صديق '),
    (family,'أسرة'),
    (neighbors,'الجيران'),
    (Google,'جوجل '),
    (Whatsapp,'واتساب'),
    (snapchat,'سناب'),
    (Instagram,'انستقرام'),
    (Twitter,'تويتر'),
    (Facebook,'فيس بوك '),
    (ticktock,'تيك توك'),
    (YouTube,'يوتيوب '), 
    (Email,'البريد الإلكتروني'),
    (Site,' موقع الإلكتروني'),
    (other,'آخر'),
        
  )  
    waiting = 'انتظار'
    Send =  'ارسل'
    CHOICES_STATUS = (( waiting,'انتظار'),(Send ,'ارسل') )


 
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    phone= models.CharField(max_length=20)
    web =models.CharField(max_length=50)  
    LandingPage = models.CharField(max_length=500)
    Doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE,blank=True, null=True)
    knew = models.CharField(max_length=50, choices=CHOICES_knew, default=Undefined)
    Message= models.CharField(max_length=500)
    STATUS = models.CharField(max_length=50, choices=CHOICES_STATUS, default=waiting )
 
    def __str__(self):
        return self.name

# Visiblenumbers Django App