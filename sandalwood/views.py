from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def kantara(request):
    return HttpResponse('<h1>Rishab Shetty is the main lead in Kantara</h1>')

def mufti(request):
    return HttpResponse('<h1>Shiva Rajkumar is the main lead in Mufti</h1>')
