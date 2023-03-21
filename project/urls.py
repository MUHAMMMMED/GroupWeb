"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('', include('accounts.urls',namespace='accounts')),
    path('', include('webs.url',namespace='webs')),
    # path('CRM/', include('CRM.url',namespace='crm')),web/

    # path('', include('Home.url',namespace='Home')), 
    # path('Doctors/', include('Doctor.url',namespace='Doctor')), 
    # path('Blog/', include('Blog.url',namespace='Blog')), 
    # path('Services/', include('Services.url',namespace='Services')), 
    # path('About/', include('About.url',namespace='About')), 
    # path('Section/', include('section.url',namespace='section')), 
 
    
    
    
    path('admin/', admin.site.urls),
#  offers/
]
# urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)