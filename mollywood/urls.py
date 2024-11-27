from django.urls import path
from mollywood.views import *

urlpatterns=[
    path('lucifer/',lucifer,name='lucifer'),
    path('kannurSquad/',kannurSquad,name='kannurSquad'),
]