from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def leo(request):
    return HttpResponse('<h1>Vijay is the main lead in Leo</h1>')

def jailer(request):
    return HttpResponse('<h1>Rajnikanth is the main lead in Jailer</h1>')

