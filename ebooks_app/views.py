from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Hello World')
# Above code home request send response logic

def contact(request):
    return HttpResponse('contact page')