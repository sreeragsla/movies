from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def devara(request):
    return HttpResponse('<h1>NTR is the main lead in Devara</h1>')

def baahubali(request):
    return HttpResponse('<h1>Prabhas is the main lead in Baahubali</h1>')


