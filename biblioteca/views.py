from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def principal(request):
    return HttpResponse("Teste")