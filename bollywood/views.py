from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jawaan(request):
    return HttpResponse('<h1>Shah Rukh Khan is the main lead in Jawaan</h1>')

def animal(request):
    return HttpResponse('<h1>Ranbir Kapoor is the main lead in Animal</h1>')

