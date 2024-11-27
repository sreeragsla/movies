from django.urls import path
from kollywood.views import *

urlpatterns=[
    path('leo/',leo,name='leo'),
    path('jailer/',jailer,name='jailer'),
]