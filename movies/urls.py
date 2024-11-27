"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tollywood.views import *
from sandalwood.views import *
from bollywood.views import *
import mollywood,kollywood

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mollywood/',include('mollywood.urls')),
    path('kollywood/',include('kollywood.urls')),
    path('kantara/',kantara,name='kantara'),
    path('mufti/',mufti,name='mufti'),
    path('devara/',devara,name='devara'),
    path('baahubali/',baahubali,name='baahubali'),
    path('jawaan/',jawaan,name='jawaan'),
    path('animal/',animal,name='animal'),
]
