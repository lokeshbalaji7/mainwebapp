"""
URL configuration for WebApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',include('firstApp.urls')),
    path('second/',include('secondApp.urls')),
    path('third/',include('ThirdApp.urls')),
    path('calculator/',include('calculator.urls')),
    path('template/',include('templateApp.urls')),
    path('db/',include('DBApp.urls')),
    path('myapp/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('fourth/',include('fourthApp.urls')),
    path('session/',include('sessionApp.urls')),
    path('form/',include('formApp.urls')),
    path('letstravel/',include('LetsTravel.urls')),
    path('pgp/',include('pgapp.urls')),
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
