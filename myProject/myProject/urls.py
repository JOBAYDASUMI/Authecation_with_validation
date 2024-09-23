
from django.contrib import admin
from django.urls import path
from myProject.views import *


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homePage,name='home'),
    path('', registrationPage,name='registrationPage'),
    path('loginPage/', loginPage,name='loginPage'),
    path('logoutPage/', logoutPage,name='logoutPage'),
    path('jobFeddPage/', jobFeddPage,name='jobFeddPage'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
