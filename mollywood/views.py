from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def lucifer(request):
    return HttpResponse('<h1>Mohan Lal is the main lead in Lucifer movie<h1>')

def kannurSquad(request):
    return HttpResponse('<h1>Mammootty is the main lead in Kannur Squad movie</h1>')

